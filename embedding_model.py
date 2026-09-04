from sentence_transformers import SentenceTransformer
import numpy as np
import json

INPUT_FILE = "data/chunks.jsonl"
OUTPUT_FILE = "data/embeddings.npy"
MODEL_NAME = "BAAI/bge-base-en-v1.5"
BATCH_SIZE = 32

def prepare_text(chunk):
    parts = []

    if chunk.get("filename"):
        parts.append(f"File name: {chunk['filename']}")
    if chunk.get("relative_path"):
            parts.append(f"Relative Path: {chunk['relative_path']}")
    if chunk.get("source"):
            parts.append(f"Source: {chunk['source']}")
    if chunk.get("effective_date"):
            parts.append(f"Effective Date: {chunk['effective_date']}")
    if chunk.get("binding"):
            parts.append(f"Binding: {chunk['binding']}")
    if chunk.get("section"): 
            parts.append(f"Section: {chunk['section']}")
    if chunk.get("text"):
            parts.append(f"Text: {chunk['text']}")

    return "\n\n".join(parts)


def embed_chunks():
    raw_chunks = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
                line = line.strip()

                if not line:
                    continue

                chunk = json.loads(line)
                raw_chunks.append(chunk)
    print(f"Loaded {len(raw_chunks)} chunks.")

    processed_chunks = [prepare_text(chunk) for chunk in raw_chunks]

    print(f"Loading Embedding model: {MODEL_NAME}")
    model = SentenceTransformer(
        MODEL_NAME,
        device = 'cpu'
    )

    print(f"Generating Embeddings")
    embeddings = model.encode(
        processed_chunks,
        batch_size = BATCH_SIZE,
        show_progress_bar = True,
        normalize_embeddings = True
    )

    embeddings = embeddings.astype("float32")

    print("\n\nEmbedding Complete")
    print(f"Total Embeddings: {len(embeddings)}")
    print(f"Embedding Dimension: {embeddings.shape[1]}")

    np.save(OUTPUT_FILE, embeddings)
    print(F"Embedding Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    embed_chunks()


