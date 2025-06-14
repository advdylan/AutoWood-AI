#!/usr/bin/env python3
# get_files.py
import os
import sys
import pathlib
from sentence_transformers import SentenceTransformer
import chromadb
from backend_scan_files import scan_folder

# ── 1. Resolve and validate the base path ────────────────────────────────────
# Allow path via CLI:  python get_files.py /absolute/or/relative/path
BASE_PATH = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../").expanduser().resolve()
if not BASE_PATH.exists():
    sys.exit(f"❌ Path does not exist: {BASE_PATH}")

print(f"📂 Indexing code under: {BASE_PATH}")

# ── 2. Initialise Chroma (embedded, persists to ./chroma_db) ────────────────
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection    = chroma_client.get_or_create_collection("codebase")

# ── 3. Prepare embedder ─────────────────────────────────────────────────────
embedder = SentenceTransformer("all-mpnet-base-v2")

# ── 4. Walk & gather docs ───────────────────────────────────────────────────

docs, metadatas, ids = scan_folder(f"{BASE_PATH}/backend/", max_depth=1,ALLOWED_EXT=[".py"])

print(f"📝 Found {len(docs)} code files/chunks")

if not docs:
    sys.exit("❌ Nothing to index. Check the directory or extensions.")

# ── 5. Embed & upload ───────────────────────────────────────────────────────
embeddings = embedder.encode(docs).tolist()


BATCH_SIZE = 5000
for i in range(0, len(docs), BATCH_SIZE):
    #print(f"Docs: {docs[i:i+BATCH_SIZE]}")
    #print(f"Docs: {embeddings[i:i+BATCH_SIZE]}")
    #print(f"Docs: {metadatas[i:i+BATCH_SIZE]}")
    #print(f"Docs: {ids[i:i+BATCH_SIZE]}")
    collection.add(
        documents=docs[i:i+BATCH_SIZE],
        embeddings=embeddings[i:i+BATCH_SIZE],
        metadatas=metadatas[i:i+BATCH_SIZE],
        ids=ids[i:i+BATCH_SIZE]
    )
    print(f"Uploaded batch {i // BATCH_SIZE + 1}")


print("✅ Finished indexing and persisted to ./chroma_db")
