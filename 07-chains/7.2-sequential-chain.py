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

# Output:
# * **Increased Focus and Flow:** Nighttime coding offers fewer distractions, promoting deeper concentration and extended periods of uninterrupted work.
# * **Potential for Better Alignment with Chronotype:**  Individuals who are naturally more productive at night can leverage their peak performance during these hours.
# * **Risk of Disrupted Sleep and Health Issues:**  Regular late-night coding can negatively impact sleep, leading to various physical and mental health problems.
# * **Social Isolation and Collaboration Challenges:** Working non-traditional hours can hinder social interaction and make collaborating with teams on standard schedules difficult.
# * **Mitigation Requires Proactive Health Management:**  Successful nighttime coding requires conscious efforts to maintain a healthy sleep schedule, diet, regular breaks, and social connections.