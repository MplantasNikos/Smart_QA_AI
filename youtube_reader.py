from imports import * 

def youtube_loader(video_url):
    loader = YoutubeLoader.from_youtube_url(video_url)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)

    text = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(text,embeddings)
    return db
