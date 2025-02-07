from query_llm import query_llama
from retrive_docs import retrieve_documents

def generate_compliance_report(query):
    retrieved_chunks = retrieve_documents(query)
    context = " ".join(retrieved_chunks[:3])  # Use top chunks

    response = query_llama(query, context)
    return response

#user_query = "How do I ensure GDPR compliance?"
#print(generate_compliance_report(user_query))
