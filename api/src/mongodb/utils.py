
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter     
from langchain.embeddings import HuggingFaceEmbeddings
from pathlib import Path
import requests
import os 

model_id = "sentence-transformers/all-MiniLM-L6-v2"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
api_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]

headers = {"Authorization": f"Bearer {api_token}"}
 
def embedding(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    print(response.content)

def extract_texts(documents):
    """Extract page_content from each document."""
    return [doc.page_content for doc in documents]
    
def vector_embedding(file):
    loader = PyPDFLoader(str(file))
    document = loader.load()
    # Compute embeddings for each document
    document_embeddings = []
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
    splits = text_splitter.split_documents(document)
    texts = extract_texts(splits)
    embedding(texts)

    return embedding


def get_pdf_files(fileName):
    utils_dir = Path(__file__).parent
    data_dir = utils_dir / fileName
    for file in os.listdir(data_dir):
        file_path = data_dir / file
        if file_path.suffix == '.pdf':
            #vector_embedding(file_path)
            return file_path
        


