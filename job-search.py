from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

load_dotenv()


tavily = TavilyClient()


@tool
def job_search(query: str) -> str:
    """This tool searches for jobs over the internet"""
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)
agent = create_agent(
    model=llm,
    tools=[job_search],
    system_prompt="You are a helpful assistant"
)


def main():
    result = agent.invoke(
        {"messages": [
            {"role": "user", "content": "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"}
        ]}
    )
    print(result['messages'][-1].text)


if __name__ == '__main__':
    main()
