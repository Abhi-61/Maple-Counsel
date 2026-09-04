from pathlib import Path
from datetime import datetime
import hashlib
import utils

source_map = {
    "Citizenship Act.md": "Department of Justice Canada",
    "Citizenship Regulations.md" : "Department of Justice Canada",
    "Immigration and Refugee Protection Act.md": "Department of Justice Canada",
    "Immigration and Refugee Protection Regulations.md": "Department of Justice Canada",
    "IRB Chairperson Guidelines": "Immigration and Refugee Board",
    "IRB Chairperson Jurisprudential Guide": "Immigration and Refugee Board",
    "Program Delivery Instructions": "Canada.ca",
    "Provincial Nominee Program": "Province PNP Website",
    "canada-immigration-document-requirements.md": "LLM Generated"
}

binding_flag = {
    "Citizenship Act.md": True,
    "Citizenship Regulations.md" : True,
    "Immigration and Refugee Protection Act.md": True,
    "Immigration and Refugee Protection Regulations.md": True,
    "IRB Chairperson Guidelines": False,
    "IRB Chairperson Jurisprudential Guide": False,
    "Program Delivery Instructions": False,
    "Provincial Nominee Program": True
}

metadata = []

def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def build_metadata():
    root = Path('Knowledge Base/MD')
    for path in root.rglob("*"):
        if path.is_file():
            filename = path.name
            relative_path = path.relative_to(root).parts[0]
            source_key = source_map.get(relative_path, relative_path)
            effective_date = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            binding = binding_flag.get(relative_path, True)
            content_hash = file_hash(path=path)
            metadata.append({
                "filename": filename,
                "relative_path": relative_path,
                "source": source_key,
                "effective_date": effective_date,
                "binding": binding,
                "content_hash": content_hash
            })

    utils.save_jsonl(filename="data/metadata.jsonl", data=metadata)
            
            


if __name__ == "__main__":
    build_metadata()