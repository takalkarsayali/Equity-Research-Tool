import os
import streamlit as st
import pickle
import time

from langchain_groq import ChatGroq

# from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env

st.title(" _:blue[EquityX AI]_: News Research Tool :chart_with_upwards_trend:")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    # st.sidebar.text_input(f"URL {i+1}") 
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store.pkl"
main_placeholder = st.empty()

if process_url_clicked:
    # Loading Data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading... Started ✅")
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size = 1000
    )
    main_placeholder.text("Text Splitting... Started ✅")
    docs = text_splitter.split_documents(data)

    # create embeddings and save it to FAISS index
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Vector Store Created ✅")
    time.sleep(2)

     # Save FAISS index
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)
