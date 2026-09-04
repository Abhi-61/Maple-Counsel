import re
from pathlib import Path
import json
import utils


def chunk_markdown(text, file_metadata):
    pattern = r'^#{1,6}\s+(.+)$'

    matches = list(re.finditer(
        pattern,
        text,
        flags=re.MULTILINE
    ))

    chunks = []

    for i, match in enumerate(matches):
        section_name = match.group(1).strip()
        start = match.start()
        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(text)
        )

        section_text = text[start:end].strip()

        chunks.append({
            "text": section_text,
            "section": section_name,
            **file_metadata
        })

    return chunks


def chunk_data():
    chunks = []
    metadata_bulk = utils.retrieve_jsonl("data/metadata.jsonl")

    root = Path('Knowledge Base/MD')
    for path in root.rglob("*"):
        if path.is_file():
            filename = path.name
            metadata = next(
                (item for item in metadata_bulk if item["filename"] == filename),
                None
            )
            with path.open("r", encoding="utf-8") as f:
                text = f.read()
                chunks.extend(chunk_markdown(text, metadata))

    return chunks

def save_chunks(filename: str):
    data = chunk_data()
    utils.save_jsonl(data=data, filename=filename)

if __name__ == "__main__":
    filename = "data/chunks.jsonl"
    save_chunks(filename=filename)

            
    
    