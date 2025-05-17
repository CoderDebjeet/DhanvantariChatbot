from src.helper import load_pdf,text_split,download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from langchain.docstore.document import Document


extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()
documents = [Document(page_content=text) for text in text_chunks]


pc = Pinecone(api_key="b7c04096-62f9-48f5-a488-88a321ac12c2")
index = pc.Index("mrdicalchatbot")

import os
os.environ['PINECONE_API_KEY']="b7c04096-62f9-48f5-a488-88a321ac12c2"
PineconeVectorStore.from_documents(documents,embeddings,index_name='mrdicalchatbot')

vectorstore=PineconeVectorStore(index_name='mrdicalchatbot',embedding=embeddings,pinecone_api_key="b7c04096-62f9-48f5-a488-88a321ac12c2")
