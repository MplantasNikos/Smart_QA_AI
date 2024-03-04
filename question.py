from imports import *



def question(query,db,k=2):
    retriever = db.as_retriever(search_type='similarity',search_kwargs={'k':k})

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(max_tokens = 200),chain_type='stuff',retriever=retriever
    )
    res = qa({"query":query})
    return res

    

