from rag_pipeline import rag_pipeline


def main():
    count = 0
    chat_history = []
    while True:
        
        prompt = input("Enter your prompt: ")

        if prompt == "End":
            break

        response, chat_history_updated = rag_pipeline(prompt, chat_history, True if count == 0 else False)
        chat_history.extend(chat_history_updated)

        print("Generating response...")
        print(f"Response:\n{response.message.content}")
        print()

        count += 1

if __name__ == "__main__":
    main()