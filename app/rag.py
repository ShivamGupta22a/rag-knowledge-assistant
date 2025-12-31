from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from openai import OpenAI

load_dotenv()

VECTOR_STORE_DIR = "vector_store"


def load_qa_chain():
    # Embeddings (same as ingestion)
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vector_store = FAISS.load_local(
        VECTOR_STORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    client = OpenAI()

    prompt = ChatPromptTemplate.from_template(
        """Answer the question using ONLY the context below.
If the answer is not in context, say "I don't know."

Context:
{context}

Question:
{question}
"""
    )

    def call_llm(prompt_value) -> str:
        # Convert LangChain prompt to plain string
        prompt_text = prompt_value.to_string()

        response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that answers using only the given context."
        },
        {
            "role": "user",
            "content": prompt_text
        }
    ]
)

        return response.choices[0].message.content

    chain = (
        {
            "context": retriever,
            "question": lambda x: x
        }
        | prompt
        | call_llm
        | StrOutputParser()
    )

    return chain
