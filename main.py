# Standard Libraries
import os
import time
import pickle
# Streamlit
import streamlit as st
# LangChain LLM
from langchain_groq import ChatGroq
# LangChain Chain 
from langchain_classic.chains import RetrievalQA
# Text Splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
# Document Loader
from langchain_community.document_loaders import UnstructuredURLLoader
# Vector Store 
from langchain_community.vectorstores import FAISS
# Embeddings 
from langchain_community.embeddings import HuggingFaceEmbeddings
# Environment 
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

# ---------------- LLM (Groq) ----------------
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.3,
    groq_api_key=os.environ["GROQ_API_KEY"]
)

if process_url_clicked:
    # ---------------- Loading Data ----------------
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading... Started ✅")
    data = loader.load()

    # ---------------- Split data ----------------
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size = 1000
    )
    main_placeholder.text("Text Splitting... Started ✅")
    docs = text_splitter.split_documents(data)

    # ---------------- create embeddings and save it to FAISS index
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Vector Store Created ✅")
    time.sleep(2)

     # ---------------- Save FAISS index ----------------
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore, f)

# ---------------- Question Answering ----------------
query = main_placeholder.text_input("Question: ")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
            )

            result = qa_chain.invoke({"query": query})

            st.header("Answer")
            st.subheader(result["result"])

 
            # Display sources, if available            
            st.subheader("Sources")

            unique_sources = set()

            for doc in result["source_documents"]:
                source = doc.metadata.get("source", "Unknown")
                unique_sources.add(source)

            for source in unique_sources:
                st.markdown(f"- [{source}]({source})")