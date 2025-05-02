# Now we shouldn't use this code. It's old and now we should use chat models.
from langchain_openai import OpenAI 
from dotenv import load_dotenv

# load the env variables e.g., API KEY
load_dotenv()

# Select LLM
llm = OpenAI(model="gpt-3.5-turbo-instruct") 

# Send a query to llm using invoke method of langchain
result = llm.invoke("What is capital of Pakistan?")

print(result)

