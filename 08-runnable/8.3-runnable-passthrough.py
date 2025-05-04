from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough, RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts

# Prompt 1 
prompt1 = PromptTemplate(
    template="Write down a joke on {topic}",
    input_variables=["topic"]
)

# Prompt 2 
prompt2 = PromptTemplate(
    template ="Explain the {text}",
    input_variables=["text"]
)

# Step 2: Model
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 3: Parser
parser = StrOutputParser()

# Step 4: chain

joke_gen_chain = RunnableSequence(prompt1, chat_model, parser)

parallel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "explanation":RunnableSequence(prompt2, chat_model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"topic":"AI"})
print(result)

print(final_chain.get_graph().print_ascii())

# Output:
# {'joke': 'Why did the AI cross the road?\n\nIt detected a statistically significant increase in the probability of improved learning opportunities on the other side.', 'explanation': "This answer plays on the idea that AI, especially machine learning models, are driven by data and optimization.  It's a humorous response because it replaces the simple, human motivation for crossing a road (e.g., to get to the other side) with a complex, data-driven rationale.  It suggests the AI isn't just crossing for a mundane reason, but because its algorithms have calculated that doing so will lead to better data, and thus, better performance.  It's funny because it's an over-the-top, overly analytical approach to a simple action."}
#                         +-------------+
#                         | PromptInput |
#                         +-------------+
#                                 *
#                                 *
#                                 *
#                        +----------------+
#                        | PromptTemplate |
#                        +----------------+
#                                 *
#                                 *
#                                 *
#                    +------------------------+
#                    | ChatGoogleGenerativeAI |
#                    +------------------------+
#                                 *
#                                 *
#                                 *
#                       +-----------------+
#                       | StrOutputParser |
#                       +-----------------+
#                                 *
#                                 *
#                                 *
#               +---------------------------------+
#               | Parallel<joke,explanation>Input |
#               +---------------------------------+
#                      ****               ***
#                   ***                      ***
#                 **                            ***
#     +----------------+                           **
#     | PromptTemplate |                            *
#     +----------------+                            *
#              *                                    *
#              *                                    *
#              *                                    *
# +------------------------+                        *
# | ChatGoogleGenerativeAI |                        *
# +------------------------+                        *
#              *                                    *
#              *                                    *
#              *                                    *
#     +-----------------+                    +-------------+
#     | StrOutputParser |                    | Passthrough |
#     +-----------------+                    +-------------+
#                      ****               ***
#                          ***         ***
#                             **     **
#               +----------------------------------+
#               | Parallel<joke,explanation>Output |
#               +----------------------------------+
# None