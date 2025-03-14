#import langchain dependencies
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

#bring in streamlit for ui dev
import streamlit as st

#bring watsonx interface
from watsonxlangchain import LangchainInterface

#setup app title
st.title('Ask Grumbot')

#build prompt input template to display prompts
prompt = st.chat_input('Pass your prompt here')

#if user hits enter
if prompt:
    #display prompt
    st.chat_message('user').markdown(prompt)