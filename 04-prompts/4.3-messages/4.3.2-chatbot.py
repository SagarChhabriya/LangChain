from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_history = [
    SystemMessage("You are a helpful ai assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == "exit":
        break 
    result = model.invoke(chat_history) 
    chat_history.append(AIMessage(result.content))
    print("AI: ", result)