
from imports import *




def pdf_reader(file):
    loader = PyPDFLoader(file)
    documents = loader.load()

    text_spliter = RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=10)
    text = text_spliter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(text,embeddings)

    return db 


