import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer

# Load symptom-department KB
entries = []
with open("medical_symptom_department_kb.txt", encoding="utf-8") as f:
    for line in f:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 3:
            entries.append(parts)  # [keywords, desc, dept]

# Encode descriptions
model = SentenceTransformer("all-MiniLM-L6-v2")
descs = [e[1] for e in entries]
embs = model.encode(descs, convert_to_numpy=True)

# Build FAISS index
dim = embs.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embs)

# Save index and metadata
with open("faiss_kb.pkl", "wb") as f:
    pickle.dump({
        "index": index,
        "entries": entries
    }, f)

print(f"✅ Built FAISS index with {len(entries)} entries.")
