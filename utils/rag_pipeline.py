import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load FAISS index
with open("faiss_kb.pkl", "rb") as f:
    data = pickle.load(f)
index, entries = data["index"], data["entries"]

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def get_department(symptoms: str) -> str:
    q_emb = embed_model.encode(symptoms, convert_to_numpy=True)
    D, I = index.search(np.array([q_emb]), k=3)
    contexts = [entries[i][1] for i in I[0]]
    context_text = " ".join(contexts)
    # Directly retrieve department metadata from best match
    top_idx = I[0][0]
    return entries[top_idx][2]
