import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings  # Ensure correct import
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    st.error("OpenAI API key is missing. Please set it in the .env file.")

# Upload PDF files

st.header("My first ChatBot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")
    
    
#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
        # st.write(text)

#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators= "\n",
        chunk_size= 1000,
        chunk_overlap= 150,
        length_function=len
    )
    
    chunks = text_splitter.split_text(text)
    st.write(chunks)