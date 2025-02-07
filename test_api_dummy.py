from flask import Flask, request, jsonify
from report import generate_compliance_report

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_rag():
    data = request.json
    user_query = data.get("query", "")
    
    if not user_query:
        return jsonify({"error": "Missing query"}), 400
    
    response = generate_compliance_report(user_query)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
