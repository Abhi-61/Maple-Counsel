from ollama import chat


def rewrite_prompt(prompt: str, chat_history: list, is_first_prompt = False):

    if is_first_prompt:
        response = chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": "Say these exact words: 'Hello there. How may I help with your concerns regarding IRCC?'"
                }
            ],
            think=False,
            keep_alive="30m"
        )
        return response.message.content

    SYSTEM_PROMPT = """
                Rewrite the user's question for semantic search in a clear and concise manner.

                Preserve the user's original intent exactly.

                Do not answer the question.
                Do not introduce new information.
                Do not remove important constraints, dates, names,
                programs, occupations, locations, or eligibility criteria.

                Return only the rewritten search query.

                Examples:
                    {User Prompt: "I am really worried about my Alberta Provincial Nominee Program Application. I do not know if I submitted all my documents correctly. Can you please help?"
                    Rewritten Prompt: "What is the required document checklist for the Alberta Provincial Nominee Program?"},

                    {User Prompt: "I have been living in Canada for 6 years on a work permit. Is it possible to get a Permanent Residency now?"
                    Rewritten Prompt: "Eligibility for Permanent Residency with Work Permit"}

                    {User Prompt: "What is the AAIP?"
                    Rewritten Prompt: "What is the AAIP?"}
    """

    response = chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                *chat_history,
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            think=False,
            options={
                "temperature": 0.1,
                "num_predict": 100,
                
            }
    )

    return response.message.content
