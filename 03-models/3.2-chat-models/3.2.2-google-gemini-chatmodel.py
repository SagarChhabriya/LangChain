from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

response = chat_model.invoke("What is the current rate of US Dollar?")

print(response.content)