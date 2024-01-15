import os
from fastapi import APIRouter, FastAPI, WebSocketDisconnect, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
import uuid
from ..socket.connection import ConnectionManager
from ..socket.utils import get_token
from ..redis.producer import Producer
from ..redis.config import Redis
from src.schemas.chat import Chat
from rejson import Path
from ..redis.stream import StreamConsumer
from ..redis.cache import Cache
from ..mongodb.config import Mongo
from ..mongodb.utils import vector_embedding, get_pdf_files
from fastapi import WebSocket
import time

chat = APIRouter()
manager = ConnectionManager()
redis = Redis()
mongo = Mongo()

# @route 
#@desc assuming you do nothing this message should appear in your localhost http://localhost:3500/
@chat.get("/")
def index():
    return {"message": "Welcome To FastAPI"}


# @route POST /create_embedding
#@desc Route to create vector embedding for mongo database
#@access PUBLIC
@chat.post("/create_embedding")
async def create_embedding(file_request: str,collection=Depends(mongo.get_collection)):
    file_directory = get_pdf_files(file_request)

    # Process each PDF file and store the results in MongoDB
    embeddings = vector_embedding(file_directory)  # Use your vector_embedding method
    data_to_insert = {
        "title": file_directory,
        "embedding": embeddings
    }
    
    await collection.insert_one(data_to_insert)

    return JSONResponse(content={"message": "PDFs processed and embeddings stored successfully"})



# @route   POST /token
# @desc    Route to generate chat token
# @access  Public
@chat.post("/token")
async def token_generator(email: str, request: Request):
    token = str(uuid.uuid4())

    if not email.endswith("@sjsu.edu"):
        raise HTTPException(status_code=400, detail={
            "loc": "name",  "msg": "Enter a valid SJSU email"})

    # Create new chat session
    json_client = redis.create_rejson_connection()
    print("Connected to DB!")

    chat_session = Chat(
        token=token,
        messages=[],
        email = email
    )

    # Store chat session in redis JSON with the token as key
    json_client.jsonset(str(token), Path.rootPath(), chat_session.dict())

    # Set a timeout for redis data
    redis_client = await redis.create_connection()
    await redis_client.expire(str(token), 3600)


    return chat_session.model_dump()



# @route   POST /refresh_token
# @desc    Route to refresh token
# @access  Public
@chat.get("/refresh_token")
async def refresh_token(request: Request, token: str):
    json_client = redis.create_rejson_connection()
    cache = Cache(json_client)
    data = await cache.get_chat_history(token)

    if data == None:
        raise HTTPException(
            status_code=400, detail="Session expired or does not exist")
    else:
        return data

# @route   Websocket /chat
# @desc    Socket for chat bot
# @access  Public
@chat.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket, token: str = Depends(get_token)):
    await manager.connect(websocket)
    redis_client = await redis.create_connection()
    producer = Producer(redis_client)
    print(token)

    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            stream_data = {}
            stream_data[token] = data
            await producer.add_to_stream(stream_data, "message_channel")
            await manager.send_personal_message(f"Response: Simulating response from the GPT service", websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)