from pathlib import Path
import json

def retrieve_jsonl(file_path: str):
    file_path = Path(file_path)
    data = []
    with file_path.open("r", encoding="utf-8") as file:
        for line in file:
            data.append(json.loads(line))

    return data

def save_jsonl(data: list, filename: str):
    with open(filename, "w") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")

def build_chat_history(chat_history: list, messages: list, response: dict):
    if len(chat_history) >= 10:
        del chat_history[:2]

    user_prompt = messages[-1]

    assistant_prompt = {"role": "assistant",
                        "content": response.message.content}

    chat_history.append(user_prompt)
    chat_history.append(assistant_prompt)

    return chat_history

    