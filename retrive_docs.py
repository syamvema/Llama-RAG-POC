import faiss
import numpy as np
from generate_store_embedding import embedding_model
from extract_chunks import all_chunks


def retrieve_documents(query, top_k=3):
    index = faiss.read_index("faiss_index.bin")
    query_embedding = np.array([embedding_model.encode(query)], dtype="float32")

    # Search for top_k similar chunks
    distances, indices = index.search(query_embedding, top_k)

    retrieved_chunks = [all_chunks[idx] for idx in indices[0]]
    return retrieved_chunks
