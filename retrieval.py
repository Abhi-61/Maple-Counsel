import os

from huggingface_hub.utils import disable_progress_bars
from huggingface_hub import logging as hf_logging
from transformers.utils import logging as transformers_logging
from transformers.utils import logging as transformers_logging

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

QDRANT_PATH = "qdrant_db"
COLLECTION_NAME = "Immigration Documents"

MODEL_NAME = "BAAI/bge-base-en-v1.5"

disable_progress_bars()
hf_logging.set_verbosity_error()
transformers_logging.set_verbosity_error()
transformers_logging.disable_progress_bar()
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"


client = QdrantClient(
        path=QDRANT_PATH
    )

model = SentenceTransformer(
MODEL_NAME,
device="cpu",
)

def retrieve(prompt: str, is_first_prompt: bool):

    if is_first_prompt:
        return prompt

    query_embedding = model.encode(
    prompt,
    normalize_embeddings=True,
    )


    RETRIEVAL_LIMIT = 5
    results = client.query_points(
    collection_name=COLLECTION_NAME,
    query=query_embedding.tolist(),
    limit=RETRIEVAL_LIMIT,
    with_payload=True,
    ).points

    retrieval_result = ""

    for i, result in enumerate(results, start=1):
        new_doc = f"Document Number: {i}\nSection: {result.payload.get("section")}\nFile: {result.payload.get("filename")}\nSource: {result.payload.get("source")}\
        \nEffective Date: {result.payload.get("effective_date")}\nContent: {result.payload.get("text")}"
        retrieval_result += new_doc
        retrieval_result += "\n\n"

    return retrieval_result




