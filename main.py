from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from retrive_docs import retrieve_documents
from fastapi import FastAPI, HTTPException
from query_llm import query_llama
import requests

app = FastAPI()

# Allow CORS for frontend (React) running on localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.post("/query")
def query_rag(request: QueryRequest):
    try:
        # Retrieve top document chunks
        retrieved_chunks = retrieve_documents(request.query)
        context = " ".join(retrieved_chunks)  # Combine chunks

        # Call Llama directly
        llm_response = query_llama(request.query, context)

        return {"response": llm_response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))