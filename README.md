# Ayurvedic-Chatbot-named Dhanvantari
Dhanvantari is an intelligent Ayurvedic assistant designed to provide personalized treatment suggestions based on user symptoms, recommend doctors and medicines, offer knowledge on herbs, and guide users in maintaining a healthy work-life balance through yoga and lifestyle tips. It integrates LLM (GPT), Retrieval-Augmented Generation (RAG), and a modern Flutter-based cross-platform UI.

🛠️ Tech Stack
Frontend: Flutter (Cross-platform)

Backend & AI:

Python (FastAPI / Flask)

HuggingFace Transformers (LLM)

Pinecone (Vector DB for semantic search)

RAGChain (for Retrieval-Augmented Generation)

Database: Firebase Firestore (for users, appointments, and preferences)

Authentication: Firebase Auth

Hosting: Firebase Hosting / Vercel (Optional for backend)

🔄 Detailed Functional Workflow
1. Symptom Input
User enters symptoms like: “I have cough and sore throat”.

UI validates input and forwards it to the backend.

2. Query Preprocessing
The input is cleaned and tokenized.

Converted to embeddings using Sentence Transformers (e.g., all-MiniLM).

3. Semantic Search via Pinecone
Embeddings are used to perform a semantic search in Pinecone Vector DB.

Relevant Ayurvedic texts, herbs, treatments, and causes are retrieved.

4. RAG (Retrieval-Augmented Generation)
RAGChain combines the user's query and the retrieved context.

Prompt is sent to an LLM (e.g., GPT-3.5, Falcon, or Mistral) hosted on Hugging Face.

Model generates a response using both context and general Ayurvedic knowledge.

5. Response Handling
The generated text is post-processed.

Sent back to the Flutter frontend for user display.

🧪 Example User Interaction
User: “I’m feeling fatigue and joint pain.”
Dhanvantari:
"Based on your symptoms, you may be experiencing early signs of Ama buildup (toxic residue). I recommend a light diet (Langhana), with herbs such as Guggulu and Ashwagandha. Would you like to see nearby Ayurvedic doctors?"

📌 Future Improvements
Fine-tune an LLM on Ayurvedic texts for domain-specific performance.

Multilingual support (Hindi, Sanskrit, Tamil).

Integrate Google Fit or Apple Health for lifestyle tracking.

Chatbot personalization using user history.
