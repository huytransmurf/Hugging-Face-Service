from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import numpy as np

app = Flask(__name__)
model = SentenceTransformer('all-MiniLM-L6-v2')  # tải model từ Hugging Face

@app.route("/embed", methods=["POST"])
def embed():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    vector = model.encode([text])[0]
    return jsonify({"vector": vector.tolist()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
