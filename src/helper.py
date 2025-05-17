import sys
import pdfplumber
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings



#Extract data from pdf
def load_pdf(directory):
    all_text = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            path = os.path.join(directory, filename)
            with pdfplumber.open(path) as pdf:
                for page in pdf.pages:
                    all_text.append(page.extract_text())
    return all_text

# Create Text chunks
def text_split(extracted_data):
    all_text = "\n".join(extracted_data)  # Combine all text into one string
    text_splitter=RecursiveCharacterTextSplitter(chunk_size =500 ,chunk_overlap =20)
    text_chunks = text_splitter.split_text(all_text)
    return text_chunks

#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings