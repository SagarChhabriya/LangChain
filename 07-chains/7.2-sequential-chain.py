# Topic ---> LLM ---> Detailed Report ---> LLM ---> Summary/key points
# Prompt1 | LLM | Parser | Prompt2 | LLM | Parser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts

# Prompt 1:
prompt1 = PromptTemplate(
    template="Write down a detailed report on {topic}",
    input_variables=["topic"]
)

# Prompt 2: 
prompt2 = PromptTemplate(
    template="Write down a 5 key point summary on {text}",
    input_variables=["text"]
)

# Step 2: Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 3: Output Parser
parser = StrOutputParser()

# Step 4: Chain 
chain = prompt1 | chat_model | parser | prompt2 | chat_model | parser
result = chain.invoke({"topic":"Coding in night"})
print(result)