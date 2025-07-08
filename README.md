# MedHelp AI Chatbot 🏥

A Retrieval-Augmented Generation (RAG) based medical assistant chatbot that helps users identify the appropriate hospital department based on their symptoms.

---

## ✨ Features

* 🩽 Natural symptom input from users
* ⚖️ FAISS + Sentence Transformers for semantic search
* ⚖️ IBM Watsonx Assistant integration with webhook + OpenAPI
* ⚡ FastAPI-style local backend using Flask
* 📅 User-friendly chatbot UI via Watson Web Chat
* ⚙️ Fully documented with OpenAPI spec for clean integration

---

## 📄 Project Structure

```bash
medical-chatbot/
├── app.py                     # Flask app serving the webhook endpoint
├── utils/
│   └── rag_pipeline.py       # RAG logic: embed symptoms + retrieve dept
├── faiss_kb.pkl              # Pre-built FAISS vector DB
├── medical_symptom_department_kb.txt  # Source KB file
├── templates/
│   └── index.html            # Dark-themed homepage with chatbot widget
├── load_kb.py                # Script to embed and build FAISS index
├── requirements.txt
└── openapi_get_department.json  # Watsonx OpenAPI spec
```

---

## 🚀 How It Works

1. User types symptoms in Watsonx Web Chat
2. Watsonx Assistant captures input and calls the webhook
3. Flask receives symptom string and passes it to `rag_pipeline`
4. FAISS searches for the most similar entry from the KB
5. Matching department is returned and displayed to the user

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/medical-chatbot.git
cd medical-chatbot
```

### 2. Set up virtual environment

```bash
python -m venv rag_env
source rag_env/bin/activate  # or .\rag_env\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Build vector index

```bash
python load_kb.py
```

### 5. Run Flask server

```bash
python app.py
```

### 6. Start ngrok tunnel (for webhook)

```bash
ngrok http 5000
```

Copy the generated URL and use it in your Watsonx Assistant OpenAPI spec.

### 7. Launch the chatbot UI

Navigate to `http://localhost:5000` to see the dark-themed chat landing page.

---

## 🛣️ Create Watsonx Assistant Template

1. Go to [watsonx Assistant](https://dataplatform.cloud.ibm.com/)
2. Create a new **assistant** project
3. Add **Actions** > Create template from scratch
4. Add a step to collect a `symptoms` slot
5. Add a step to **call a webhook**

   * Import the `openapi_get_department.json` file
   * Make sure the webhook uses POST to `/get_department`
   * Bind the request body to:

     ```json
     {
       "symptoms": "<?slots.symptoms?>"
     }
     ```
6. Add a response step:

   ```
   Based on your symptoms, you should consult the <?webhook.department?>.
   ```
7. Test in preview and deploy to Web Chat

---

## 🛍️ Technologies Used

* IBM Watsonx Assistant
* Flask
* FAISS
* SentenceTransformers
* ChromaDB (optional)
* Ngrok

---

## 📚 Knowledge Base Format

```txt
symptom keyword | description | department
```

Example:

```
severe dehydration | Suffering from severe dehydration started for two hours. | Emergency Department (ED)
```

---

## 📊 Example Chat Flow

```
User: I have severe dehydration and vomiting
Bot: Based on your symptoms, you should consult the Emergency Department (ED).
```

---

## ✨ Future Improvements

* Appointment booking feature
* Save chat history
* Multilingual support
* Deploy to Render/Railway for public access

---

## 🙏 Acknowledgements

* [IBM watsonx Assistant](https://www.ibm.com/products/watsonx-assistant)
* [SentenceTransformers](https://www.sbert.net/)
* [FAISS by Facebook](https://github.com/facebookresearch/faiss)

---

* Preview of the website
* ![image](https://github.com/user-attachments/assets/eeb408db-b00a-4f5c-b3e8-2742aba79baf)
* Now click the blue chat icon in the bottom right to start your query
* ![image](https://github.com/user-attachments/assets/16a53ed3-ffe0-48fa-8094-757ebbcb6549)

  


