import fitz  # PyMuPDF
import os
import tiktoken

def extract_text_from_pdfs(pdf_folder):
    documents = []
    
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_folder, file)
            doc = fitz.open(pdf_path)
            text = "\n".join([page.get_text("text") for page in doc])
            documents.append(text)
    
    return documents

# Load PDFs
pdf_folder = "./pdfs"
documents = extract_text_from_pdfs(pdf_folder)

# Tokenizer for chunking
tokenizer = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, chunk_size=512, overlap=100):
    tokens = tokenizer.encode(text)
    chunks = []
    
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = tokens[i:i + chunk_size]
        chunks.append(tokenizer.decode(chunk))
    
    return chunks

# Apply chunking to all documents
all_chunks = []
for doc in documents:
    all_chunks.extend(chunk_text(doc))
