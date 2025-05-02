from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break 
    result = model.invoke(chat_history) # send the complete chat history to the model
    chat_history.append(result)
    print("AI: ", result.content)

# Example:
# You: which one is bigger 3 or 7                                                                                               
# AI:  7 is bigger than 3.
# You: multipy the bigger number with 10 and give me the result
# AI:  7 * 10 = 70
