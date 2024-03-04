from langchain_community.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import OpenAI
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
import glob
from langchain_community.document_loaders import YoutubeLoader
import openai
from langchain_community.vectorstores import FAISS
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import UnstructuredPowerPointLoader
import pptx
from pptx import Presentation
from langchain.docstore.document import Document







import os
