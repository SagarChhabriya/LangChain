# Document ---> Notes + Quiz ---> User
# Document ---> Model1 for notes + Model2 for Quiz ---> Model3 for merging the output

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel

load_dotenv()

# Step 1: Prompts

# Prompt 1:
prompt1 = PromptTemplate(
    template="Write down the notes on {text}",
    input_variables=["text"]
)

prompt2 = PromptTemplate(
    template="Generate 5 short questions on {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the given notes and quiz into a single \n notes: {notes} \n quiz:{quiz}",
    input_variables=["notes","quiz"]
)

# Step 2: Model 
chat_model_1 = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
chat_model_2 = ChatGoogleGenerativeAI(model="gemma-3-1b-it")

# Step 3: Output Parser
parser = StrOutputParser()

# Step 4: Chain (ParallelChain)
parallel_chain = RunnableParallel(
   {
    "notes": prompt1 | chat_model_1 | parser,
    "quiz":  prompt2 | chat_model_2 | parser
    }
)


merge_chain = prompt3 | chat_model_1 | parser

chain = parallel_chain | merge_chain 

with open(r"D:\Ao\Code\GenAI\LangChain\07-chains\7.3-text.txt", "r") as file:
    result = chain.invoke({"text" : file.readlines()})
    print(result)

print(chain.get_graph().print_ascii())

# Output:
## LangChain Notes & Quiz

# **What is LangChain?**

# LangChain is an open-source framework for developing applications powered by large language models (LLMs). It connects LLMs to other resources like tools, APIs, and data sources, allowing for the creation of intelligent, multi-step applications.       

# **Why Do We Need LangChain?**

# LLMs have limitations: they can't access real-time data, remember past conversations, or interact with external systems directly. LangChain addresses these shortcomings by abstracting away the complexities of integrating LLMs with other resources.  It simplifies the development of functional and intelligent applications with minimal custom code.

# **Beginner-Friendly Example:**

# Imagine an online bookstore chatbot built using LangChain. It could:

# * Recommend books
# * Check stock availability
# * Place orders

# LangChain achieves this by connecting an LLM to the bookstore's inventory database and order system, orchestrating the entire process through structured workflows.

# **Core Concepts:**

# * **Chains:** Sequences of steps where each component's output feeds into the next.  Types include:
#     * *Sequential Chains:* Steps execute in order (e.g., Question → Search → Summarize → Answer).
#     * *Parallel Chains:* Tasks run concurrently (e.g., Summarize and extract keywords simultaneously).
#     * *Conditional Chains:* Flow depends on input (e.g., route to different tools based on query type).
# * **Model-Agnostic Design:** Easily swap LLM providers (OpenAI, Anthropic, etc.) with minimal code changes.  Example: `llm = OpenAI()  # Switch to: llm = Anthropic()`
# * **Memory and State Handling:**  LangChain incorporates memory modules to maintain context throughout conversations, enabling the application to recall previous interactions and user preferences.

# **Ecosystem Highlights:**

# LangChain provides:

# * Prompt templates
# * Integration with vector stores (e.g., Pinecone, Weaviate)
# * Tool and API connectors
# * Memory modules
# * Agents for dynamic, multi-step decision-making

# **What You Can Build:**

# | Application        | Example Use Case             |
# |-------------------|------------------------------|
# | Conversational Chatbots | Virtual assistants, support bots |
# | Knowledge Assistants | Internal document Q&A tools    |
# | AI Agents          | Multi-step task executors      |
# | Workflow Automation   | Data pipelines, report generation |
# | Summarization Tools  | Research digesters, meeting note creators |

# **Alternatives to LangChain:**

# * **LlamaIndex:**  Excellent for retrieval-augmented generation (RAG) and document Q&A.
# * **Haystack:**  Suitable for building NLP pipelines with traditional and neural search.

# LangChain excels in building complex, LLM-centric workflows.  Alternatives might offer simpler solutions for specific tasks.  


# **Quiz - Test Your Understanding:**

# 1. **What is the primary purpose of LangChain?**  (Focus: Core Purpose)
# 2. **What does "Chains" in LangChain allow developers to do?** (Focus: Key Concept)
# 3. **Which type of chain is supported by LangChain?** (Focus: Chain Types)  *(Give at least one example)*
# 4. **What is the role of memory modules in LangChain?** (Focus: Memory Handling)
# 5. **Besides LLMs, what other tools and providers can LangChain connect to?** (Focus: Ecosystem Highlights)  *(Give at least two examples)*
#                     +---------------------------+
#                     | Parallel<notes,quiz>Input |
#                     +---------------------------+
#                        ***                   ***
#                    ****                         ****
#                  **                                 **
#     +----------------+                          +----------------+
#     | PromptTemplate |                          | PromptTemplate |
#     +----------------+                          +----------------+
#              *                                           *
#              *                                           *
#              *                                           *
# +------------------------+                  +------------------------+
# | ChatGoogleGenerativeAI |                  | ChatGoogleGenerativeAI |
# +------------------------+                  +------------------------+
#              *                                           *
#              *                                           *
#              *                                           *
#     +-----------------+                         +-----------------+
#     | StrOutputParser |                         | StrOutputParser |
#     +-----------------+                         +-----------------+
#                        ***                   ***
#                           ****           ****
#                               **       **
#                     +----------------------------+
#                     | Parallel<notes,quiz>Output |
#                     +----------------------------+
#                                    *
#                                    *
#                                    *
#                           +----------------+
#                           | PromptTemplate |
#                           +----------------+
#                                    *
#                                    *
#                                    *
#                       +------------------------+
#                       | ChatGoogleGenerativeAI |
#                       +------------------------+
#                                    *
#                                    *
#                                    *
#                           +-----------------+
#                           | StrOutputParser |
#                           +-----------------+
#                                    *
#                                    *
#                                    *
#                       +-----------------------+
#                       | StrOutputParserOutput |
#                       +-----------------------+
# None