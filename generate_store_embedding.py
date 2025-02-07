import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from extract_chunks import all_chunks

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Convert chunks to embeddings
embeddings = np.array([embedding_model.encode(chunk) for chunk in all_chunks], dtype="float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save FAISS index
faiss.write_index(index, "faiss_index.bin")
