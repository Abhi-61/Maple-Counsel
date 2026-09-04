from rewrite_prompt import rewrite_prompt
from retrieval import retrieve
from generate import generate



def rag_pipeline(prompt: str, chat_history: list, is_first_prompt = False):
    rewritten_prompt = rewrite_prompt(prompt, chat_history=chat_history, is_first_prompt=is_first_prompt)

    retrieved_documents = retrieve(rewritten_prompt, is_first_prompt)

    response, chat_history = generate(prompt, retrieved_documents, chat_history, is_first_prompt)

    return response, chat_history
