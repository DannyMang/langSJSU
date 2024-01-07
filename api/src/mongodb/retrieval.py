
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter     
from langchain.embeddings import HuggingFaceEmbeddings 

class Retreival:
    def __init__(self, mongoInstance):
        self.mongoInstance = mongoInstance
    
    def vector_embedding(file):
        loader = PyPDFDirectoryLoader(file)
        documents = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
        splits = text_splitter.split_documents(documents)

        # Obtain vector embeddings using Hugging Face model
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                        model_kwargs={'device': 'cpu'})

        # Compute embeddings for each text chunk
        chunk_embeddings = []
        for split in splits:
            chunk_embedding = embeddings.embed(split)
            chunk_embeddings.append(chunk_embedding)

        return chunk_embeddings
        
