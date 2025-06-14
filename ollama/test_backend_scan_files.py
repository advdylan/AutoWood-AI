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

path = f"{BASE_PATH}/backend/"
print(path)

docs, metadatas, ids = scan_folder(path, max_depth=1,ALLOWED_EXT=(".py",))