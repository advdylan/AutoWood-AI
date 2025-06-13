from sentence_transformers import SentenceTransformer
import chromadb
from ollama import Client

# 1️⃣  Chroma server must be running in another terminal:
#     chroma run --path ./chroma_db
#     (default API endpoint: http://localhost:8000)

# 2️⃣  Initialise clients
chroma_client = chromadb.HttpClient(host="http://localhost:8000")
collection     = chroma_client.get_or_create_collection("codebase")   # <-- use the real name
embedder       = SentenceTransformer("all-MiniLM-L6-v2")
ollama_client  = Client(host="http://localhost:11434")

# 3️⃣  Chat loop

user_question = input("Ask a question about your codebase: ")
while user_question != "STOP":
    # --- embed & search ---
    query_vec = embedder.encode([user_question]).tolist()[0]
    results   = collection.query(query_embeddings=[query_vec], n_results=5)

    retrieved_docs  = results["documents"][0]
    retrieved_paths = results["metadatas"][0]

    print(f"{retrieved_docs}")

    # --- build prompt ---
    context = ""
    for doc, meta in zip(retrieved_docs, retrieved_paths):
        context += f"\n# File: {meta['path']}\n{doc}\n"

    prompt = f"""You are an expert developer. The following code snippets come from a codebase:

    {context}

    User question:
    {user_question}

    Answer in detail based on the code context.
    """

    response = ollama_client.chat(
        model="deepseek-coder:6.7b-instruct-q4_K_M",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\n🧠 Deepseek Answer:\n")
    print(response["message"]["content"])
    user_question = input("Ask a question about your codebase: ")