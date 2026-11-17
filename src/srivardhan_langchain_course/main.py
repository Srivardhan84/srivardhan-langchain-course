from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
    information = """
    Elon Musk is CEO of Tesla and SpaceX.
    """

    summary_template = """
    Given the information {information} about a person,
    create:
    1. A short summary
    2. Two interesting facts
    """

    prompt = PromptTemplate(
        input_variables=["information"],
        template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )
    
    # llm = ChatOllama(
    #     model="gemma3:270m",
    #     temperature=0
    # )

    chain = prompt | llm

    response = chain.invoke(
        {"information": information}
    )

    print(response.content)

if __name__ == "__main__":
    main()