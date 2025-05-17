# 🧘‍♂️ Dhanvantari - Your Ayurvedic Companion

**Dhanvantari** is an intelligent Ayurvedic assistant designed to provide **personalized treatment suggestions** based on user symptoms. It recommends **doctors and medicines**, shares knowledge about **herbs**, and guides users toward a **balanced lifestyle** through **yoga and wellness tips**.  
It integrates **LLM (GPT)**, **Retrieval-Augmented Generation (RAG)**, and a **modern Flutter-based cross-platform UI** for a seamless and holistic experience.

---

## 🚀 Tech Stack

| Layer         | Tools & Frameworks                                                                 |
|---------------|------------------------------------------------------------------------------------|
| **Frontend**  | Flutter (Cross-platform: Android, iOS, Web)                                        |
| **Backend**   | Python (FastAPI / Flask)                                                           |
| **AI / NLP**  | Hugging Face Transformers (LLM), RAGChain, Sentence Transformers (`all-MiniLM`)    |
| **Vector DB** | Pinecone (Semantic search with vector embeddings)                                  |
| **Database**  | Firebase Firestore (Users, Appointments, Preferences)                              |
| **Auth**      | Firebase Authentication                                                            |
| **Hosting**   | Firebase Hosting / Vercel *(optional for backend deployment)*                      |

---

## 🔄 Functional Workflow

1. ### 📝 Symptom Input
   - Users input their symptoms (e.g., "I have cough and sore throat").
   - Input is validated in the Flutter UI and sent to the backend.

2. ### 🔍 Query Preprocessing
   - Input is cleaned and tokenized.
   - Embeddings are generated using **Sentence Transformers** like `all-MiniLM`.

3. ### 🧠 Semantic Search (Pinecone)
   - The embeddings are used to search in the **Pinecone Vector DB**.
   - Relevant Ayurvedic treatments, causes, and herbs are retrieved.

4. ### 🤖 RAG (Retrieval-Augmented Generation)
   - **RAGChain** merges the user's query with the retrieved context.
   - The combined prompt is sent to an LLM (e.g., GPT-3.5, Falcon, Mistral) on **Hugging Face**.
   - The model responds with context-aware Ayurvedic guidance.

5. ### 📤 Response Handling
   - Post-processing is done on the output.
   - The final result is displayed beautifully on the Flutter frontend.

---

## 💬 Example User Interaction

> **User**: “I’m feeling fatigue and joint pain.”  
> **Dhanvantari**:  
> *"Based on your symptoms, you may be experiencing early signs of **Ama** buildup (toxic residue). I recommend a light diet (**Langhana**), with herbs such as **Guggulu** and **Ashwagandha**. Would you like to see nearby Ayurvedic doctors?"*

---

## 📸 Screenshots

<!-- Add your actual image paths here after uploading to repo -->

![Home Screen](![365042320-d44a692d-5aa2-4e6c-b0f7-3f672f9fbfd9](https://github.com/user-attachments/assets/5de03165-85fe-46dc-b115-dc1a7006f924)
)
![Chatbot Response](![jsehhseiisefsf](https://github.com/user-attachments/assets/7723518c-8b28-4d18-a5cf-8c90e57ddf87))

---

## 📌 Future Improvements

- 🔧 Fine-tune a domain-specific LLM on Ayurvedic literature.
- 🌐 Multilingual Support (Hindi, Sanskrit, Tamil).
- 📊 Google Fit / Apple Health integration for lifestyle tracking.
- 🧠 Personalized chat using user medical history.
- 📱 Add Doctor Appointment Booking & Notifications.

---

## 🙏 Why Dhanvantari?

Named after the Hindu deity of Ayurveda, **Dhanvantari** aims to **bridge ancient wisdom with modern AI**, making holistic health **accessible, personalized, and tech-driven**.
