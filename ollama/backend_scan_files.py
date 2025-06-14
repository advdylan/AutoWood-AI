import os
import pathlib

def scan_folder(base_path, max_depth, ALLOWED_EXT):
    docs, metadatas, ids = [], [], []
    
    for root, dirs, files in os.walk(base_path):
        # Skipping __ folders
        if any(part.startswith('__') for part in root.split(os.sep)):
            print(f"Skipping directory with __: {root}")
            continue

        # Calculate current depth
        current_depth = root[len(str(base_path)):].count(os.sep)
        
        if current_depth > max_depth:
            continue
            
        print(f"\nIn folder: {root} (depth {current_depth})")
        print(f"Files: {files}\n")

        for file in files:
            # Ensure ALLOWED_EXT is treated as tuple
            allowed_extensions = tuple(ALLOWED_EXT) if isinstance(ALLOWED_EXT, list) else ALLOWED_EXT
            if file.lower().endswith(allowed_extensions):
                full_path = pathlib.Path(root) / file
                try:
                    text = full_path.read_text(encoding="utf-8", errors="replace")
                except Exception as e:
                    print(f"⚠️  Skipping {full_path}: {e}")
                    continue

                docs.append(text)
                metadatas.append({"path": str(full_path.relative_to(base_path))})
                ids.append(f"doc_{len(ids)}")

        # Prevent going deeper than max_depth
        if current_depth == max_depth:
            dirs[:] = []
    
    return docs, metadatas, ids  # Moved outside the loop!

# Usage (in your test file):
#docs, metadatas, ids = scan_folder(path, max_depth=1, ALLOWED_EXT=(".py",))  # Note the tuple syntax