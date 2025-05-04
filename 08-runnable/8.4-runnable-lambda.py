#                                                _______ Passthrough
#                                               /
#   prompt --------> LLM ---------> Parse
#                                               \________ RunnableLambda(_preprocess(countwords)_)
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

# Step 1: Prompts
prompt1 = PromptTemplate(
    template="Write down a joko on {topic}",
    input_variables=["topic"]
)

# Step 2: Model
chat_model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# Step 3: Parser
parser = StrOutputParser()

# Step 4: chain
joke_gen_chain = RunnableSequence(prompt1, chat_model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
   "word_count": RunnableLambda(lambda x : len(x))
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic":"Algorithms"})
print(result)


# Output:
# {'joke': 'Why do programmers prefer dark mode? \n\nBecause light attracts bugs, and the only bugs they want are in their algorithms.', 'word_count': 120}
