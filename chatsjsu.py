import os 
from dotenv import load_dotenv,find_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_python_agent
from langchain.llms.openai import OpenAI 
from langchain.document_loaders import PyPDFLoader


#api keys 
load_dotenv(find_dotenv())
openAIKey = os.environ.get("OPEN_AI_KEY")
huggingfaceKey = os.environ.get("HUGGINGFACEHUB_API_TOKEN")



