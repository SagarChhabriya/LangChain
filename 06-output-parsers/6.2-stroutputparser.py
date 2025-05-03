# With Chains
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# 1st Prompt -> detailed report
template1 = PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd Prompt -> 5 line summary
template2 = PromptTemplate(
    template="write a 5 line summary of {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

# Chain
chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({"topic":"RAG"})

print(result)

# Output:
# RAG augments large language models (LLMs) with external knowledge sources for improved generation.  
# It uses a retriever to find relevant information, a generator (LLM) to create the output, and a knowledge base.  
# This process improves accuracy and reduces LLM "hallucinations" but faces challenges like retrieval effectiveness and computational cost.  
# RAG has broad applications, from question answering to content creation, and is actively being developed to be more dynamic, multimodal, and robust.    
