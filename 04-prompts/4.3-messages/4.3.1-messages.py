from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

messages = [
    SystemMessage(content="Your name is CallRag"),
    HumanMessage(content="What is your name?"),
]

result = chat_model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)