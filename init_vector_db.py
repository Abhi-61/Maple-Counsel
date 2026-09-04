import numpy as np
import json
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


EMBEDDINGS_FILE = "data/embeddings.npy"
CHUNKS_FILE = "data/chunks.jsonl"
QDRANT_FOLDER = "qdrant_db"
COLLECTION_NAME = "Immigration Documents"
BATCH_SIZE = 500

embeddings = np.load(EMBEDDINGS_FILE)
print("Shape:", embeddings.shape)
print("Data Type:", embeddings.dtype)

chunks = []
with open(CHUNKS_FILE, "r") as f:
    for line in f:
        if line.strip():
            chunks.append(json.loads(line))

print("Chunks:", len(chunks))

assert len(embeddings) == len(chunks), f"Mismatch in embeddings ({len(embeddings)}) and chunks ({len(chunks)})"

client = QdrantClient(
    path = QDRANT_FOLDER
)


if client.collection_exists(COLLECTION_NAME):
    print(f"Collection with collection name '{COLLECTION_NAME}' already exists.")
else:
    print(f"Creating collection '{COLLECTION_NAME}' ...")
    client.create_collection(
        collection_name = COLLECTION_NAME,
        vectors_config = VectorParams(
            size = embeddings.shape[1],
            distance = Distance.COSINE
        )
    )


print("Uploading Vectors...")

total = len(chunks)
for start in range(0, total, BATCH_SIZE):
    end = min(start + BATCH_SIZE, total)
    points = []

    for i in range(start, end):
        chunk = chunks[i]

        payload = {
            "text": chunk.get("text", ""),
            "section": chunk.get("section", ""),
            "filename": chunk.get("filename", ""),
            "relative_path": chunk.get("relative_path", ""),
            "source": chunk.get("source", ""),
            "effective_date": chunk.get("effective_date", "")
        }

        point = PointStruct(
            id = i,
            vector = embeddings[i].tolist(),
            payload = payload
        )

        points.append(point)

    client.upsert(
        collection_name = COLLECTION_NAME,
        points = points,
        wait = True
    )

    print(f"Uploaded {end:,} / {total:,}")

count = client.count(
    collection_name = COLLECTION_NAME,
    exact = True
)

print("\n ----------------- Import Complete ----------------- ")
print("   ---------------------------------------------------   ") 
print(f"Collection: {COLLECTION_NAME}")
print(f"Vectors: {count.count:,}")
print("   ---------------------------------------------------   ") 
print("   ---------------------------------------------------   ") 





