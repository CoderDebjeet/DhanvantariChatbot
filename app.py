from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from src.helper import load_pdf,text_split,download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from src.prompt import *
import os
from langchain_pinecone import Pinecone
from langchain_huggingface import HuggingFaceEmbeddings
from src.helper import load_pdf,text_split,download_hugging_face_embeddings

app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()  # Loads environment variables from .env file


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')


embeddings = download_hugging_face_embeddings()

#Initializing the Pinecone

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
#pc = Pinecone(api_key="b7c04096-62f9-48f5-a488-88a321ac12c2")
#index = pc.Index("mrdicalchatbot")
documents = [Document(page_content=text) for text in text_chunks]
#Loading the index
import os
os.environ['PINECONE_API_KEY']="b7c04096-62f9-48f5-a488-88a321ac12c2"
PineconeVectorStore.from_documents(documents,embeddings,index_name='mrdicalchatbot')

vectorstore=PineconeVectorStore(index_name='mrdicalchatbot',embedding=embeddings,pinecone_api_key="b7c04096-62f9-48f5-a488-88a321ac12c2")

from langchain.prompts import ChatPromptTemplate
template="""
Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

PROMPT=PromptTemplate(template=template, input_variables=["context", "question"])

chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':712,
                          'temperature':0.8})


retriever5 = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 1, "fetch_k": 2, "lambda_mult": 0.5},
)
qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type="stuff",  # Ensure this is a valid chain type
    retriever=retriever5,
)

@app.route("/")
def index():
    return render_template('chat.html')



@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])



if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)