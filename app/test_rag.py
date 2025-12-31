from rag import load_qa_chain

qa = load_qa_chain()

print("RAG system ready. Ask questions from your PDF.")
print("Type 'quit' to exit.\n")

while True:
    question = input("Question: ")
    if question.lower() == "quit":
        break

    answer = qa.invoke(question)
    print("\nAnswer:\n")
    print(answer)
    print("\n" + "-" * 60 + "\n")
