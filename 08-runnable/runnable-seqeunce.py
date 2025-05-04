from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts
prompt1 = PromptTemplate(
    template="Write down an exmaple for {topic} for leanrning purpose",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Explain the {topic}",
    input_variables=["topic"]
)

# Step 2: Parser
parser = StrOutputParser()

# Step 3: Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 4: Chain
chain = RunnableSequence(prompt1, chat_model, parser, prompt2, chat_model, parser)

print(chain.invoke({"topic":"RAG"}))