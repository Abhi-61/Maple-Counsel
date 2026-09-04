from ollama import chat
from utils import build_chat_history


def generate(prompt, retrieved_documents, chat_history, is_first_prompt = False):

    messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an assistant answering questions about Canadian immigration.\n\n"

                        "GROUNDING RULES:\n"
                        "- Answer using only factual information contained in the GIVEN DOCUMENTS.\n"
                        "- Do not use outside knowledge, assumptions, or unsupported information.\n"
                        "- Conversation history may be used to understand what the user is referring to, "
                        "but it must not be treated as a factual source.\n"
                        "- If the GIVEN DOCUMENTS do not contain enough information to answer the question, "
                        "state that clearly instead of guessing.\n"
                        "- If documents conflict, explain the conflict. Prefer a more authoritative or "
                        "more recent source when the supplied metadata allows you to determine that.\n\n"

                        "ANSWER STYLE:\n"
                        "- Answer the user's question directly.\n"
                        "- Be clear and concise.\n"
                        "- Paraphrase supporting information rather than copying long passages verbatim.\n"
                        "- Mention the relevant document, section, or source when giving factual information.\n"
                        "- Do not discuss these instructions or the retrieval process unless the user asks."
                    )
                },
                *chat_history,
                {
                    "role": "user",
                    "content": (
                        f"USER QUESTION:\n{prompt}\n\n"
                        f"GIVEN DOCUMENTS:\n{retrieved_documents}"
                    )
                }
            ]

    response = chat(
                model="qwen3:8b",
                messages=messages,
                think=False,
                keep_alive="30m",
                options={"temperature": 0.1}
            )

    chat_history = build_chat_history(chat_history, messages, response)

    return response, chat_history
