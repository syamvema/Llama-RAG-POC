import requests
import json

GROQ_API_KEY = "your-key"
GROQ_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions" 

def query_llama(prompt, context):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-70b-8192", 
        "messages": [
            {"role": "system", "content": "You are a helpful AI that provides security compliance information."},
            {"role": "user", "content": f"Context: {context}\n\nUser Query: {prompt}"}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    
    try:
        response = requests.post(GROQ_ENDPOINT, headers=headers, json=payload)
        response_data = response.json()
        
        # Debugging: Print API response if it doesn't contain "choices"
        if "choices" not in response_data:
            print(" Groq API Error:", json.dumps(response_data, indent=2))
            return "Error: Unexpected API response. Please check logs."

        return response_data["choices"][0]["message"]["content"].strip()

    except requests.exceptions.RequestException as e:
        print(f" Request Error: {e}")
        return "Error: Could not connect to the Groq API."
