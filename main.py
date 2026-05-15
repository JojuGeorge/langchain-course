import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)


def main():
    print("Hello from langchain-course!")
    # response = llm.invoke("Hello there.")
    # print(response)
    # print(response.content)


if __name__ == "__main__":
    main()
