from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts

# Prompt 1: Facebook Post
prompt1 = PromptTemplate(
   template="Write down a blog on {topic} for my post on medium",
    input_variables=["topic"]
)

# Prompt 2: Insta post
prompt2 = PromptTemplate(
    template="Write down a script on {topic} for my post on linkedin",
    input_variables=["topic"]
)

# Step 2: Model
chat_model_1 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
chat_model_2 = ChatGoogleGenerativeAI(model="gemma-3-1b-it")

# Step 3: Parser
parser = StrOutputParser()

# Step 4: Chain

parallel_chain = RunnableParallel({
    "facebook":RunnableSequence(prompt1, chat_model_1, parser),
    "insta": RunnableSequence(prompt2, chat_model_2, parser)
})

responses = parallel_chain.invoke({"topic":"RAG"})

print(responses["facebook"])
print(responses["insta"])