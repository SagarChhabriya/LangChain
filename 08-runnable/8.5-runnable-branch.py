# Conditional Chain == RunnableBranch

# Generates a story about a given topic
# Summarizes it only if it's long (more than 50 words)
# Otherwise, returns the original story

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts

prompt1 = PromptTemplate(
    template="Write down a detailed report on {topic}", 
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the given: \n {text}",
    input_variables=["text"]
)


# Step 2: Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 3: Parser
parser = StrOutputParser()

# Step 4: Chain
story_chain = prompt1 | chat_model | parser

# Step 5: Branch - summarize if story is long
branch_chain = RunnableBranch(
    # (condition, runnable)
    # default
    (lambda story: len(story.split()) > 50, prompt1 | chat_model | parser),
    RunnablePassthrough()
)

# Step 6: Final chain: generate story, then maybe summarize
final_chain = story_chain | branch_chain

result = final_chain.invoke({"topic": "a robot learning emotions"})
print(result)