from imports import *



def text_loaders(file):
    loader = TextLoader(file, encoding = 'UTF-8')
    documents = loader.load()

    text_spliter = RecursiveCharacterTextSplitter(chunk_size=800,chunk_overlap=10)
    text = text_spliter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(text,embeddings)
    return db