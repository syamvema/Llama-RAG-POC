import React, { useState } from "react";
import axios from "axios";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleQuerySubmit = async () => {
    if (!query) return;
    setLoading(true);
    setResponse("");

    try {
      const res = await axios.post("http://127.0.0.1:5000/query", { query });
      setResponse(res.data.response);
    } catch (error) {
      setResponse("Error fetching response. Please try again.");
    }

    setLoading(false);
  };

  return (
    <div style={{ maxWidth: "700px", margin: "50px auto", textAlign: "left" }}>
      <h2>GCP Security Compliance Assistant</h2>
      <textarea
        rows="3"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a security policy question..."
        style={{ width: "100%", padding: "10px", fontSize: "16px" }}
      />
      <br />
      <button
        onClick={handleQuerySubmit}
        style={{ padding: "10px 20px", fontSize: "16px", marginTop: "10px" }}
      >
        {loading ? "Processing..." : "Get Answer"}
      </button>
      
      {/* Render formatted response */}
      <div style={{ marginTop: "20px", padding: "10px", background: "#f8f8f8", borderRadius: "8px" }}>
        <h3>Response:</h3>
        {response ? (
          <div>
            {response.split("\n").map((line, index) => {
              if (line.startsWith("**")) {
                return <h4 key={index} style={{ marginTop: "10px" }}>{line.replace(/\*\*/g, "")}</h4>;
              } else if (line.startsWith("-")) {
                return <ul key={index}><li>{line.replace("-", "").trim()}</li></ul>;
              } else {
                return <p key={index}>{line}</p>;
              }
            })}
          </div>
        ) : (
          <p>Awaiting query...</p>
        )}
      </div>
    </div>
  );
}

export default App;
