from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# .env file must contain api key in a variable named OPENAI_API_KEY
load_dotenv()

# Load Chat Model
chat_model = ChatOpenAI(model="gpt-4")


# chat_model = ChatOpenAI(model="gpt-4", temperature)

# temperature is parameter that controls the randomness of a lanuguage model's output. 
# It affects how creative or deterministic the responses are. (temp range: 0-2)
# Lower values (0.0 - 0.3) → More determinstic and predictable
# Higher Values (0.7 - 1.5) → More random, creative, and diverse
 



# Send a query to ChatModel using invoke method of langchain
result = chat_model.invoke("What is the capital of pakistan?")

# Check the output of both statements
print(result)
print(result.content) 


# temperature
# Use Case                                      Recommended Temperature
# Factual answers (math, code, facts)               0.0 - 0.3
# Balanced responses (general QA, explanations)     0.5 - 0.7
# Creative writing, storytelling, jokes             0.3 - 1.2
# Maximum randomness (wild ideas, brainstorming)    1.5+