from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

# Step 1: Prompt
prompt = PromptTemplate(
    template="Write down a short poem on {topic}",
    input_variables=["topic"]
)

# Step 2: Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 3: Output Parser
parser = StrOutputParser()

# Step 4: Chain using langchain expression language (llel)
chain = prompt | chat_model | parser

# Step 5: Invoke the chain
result = chain.invoke({"topic":"coding"})
print(result)

# We can also visualize the chains
chain.get_graph().print_ascii()

# Output:
# With logic's grace, a dance of keys,
# A symphony of ones and zeros, please.
# From cryptic lines, a world takes form,
# A digital creation, safe and warm.
# Code compiles, a silent hum,
# A universe built, by finger and thumb.
#       +-------------+      
#       | PromptInput |
#       +-------------+
#              *
#              *
#              *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#              *
#              *
#              *
# +------------------------+
# | ChatGoogleGenerativeAI |
# +------------------------+
#              *
#              *
#              *
#     +-----------------+
#     | StrOutputParser |
#     +-----------------+
#              *
#              *
#              *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+