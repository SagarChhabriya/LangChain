# Currently Free of Cost API
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables (ensure GOOGLE_API_KEY is in .env)
load_dotenv()

# Initialize the LLM (non-chat) model
llm = GoogleGenerativeAI(model="gemini-1.5-pro")

# Use invoke to send a prompt
result = llm.invoke("What is the capital of Pakistan?")

# Print the result
print(result)
