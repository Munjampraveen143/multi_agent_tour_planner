from langchain_ollama import ChatOllama

from config.settings import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TEMPERATURE
)


llm = ChatOllama(
    model=OLLAMA_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=TEMPERATURE,
    num_predict=500
)


def ask_llm(prompt: str) -> str:

    response = llm.invoke(prompt)

    return response.content