from ollama import chat

response = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "What happens after receiving an AAIP nomination?"
        }
    ],
    think=False
)

print(response.message.content)