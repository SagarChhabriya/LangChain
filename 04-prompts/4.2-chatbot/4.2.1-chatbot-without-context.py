from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break 
    result = model.invoke(user_input) # send the static prompt
    print("AI: ", result.content)

# Example:
# You: which one is bigger 3 or 7
# AI:  7 is bigger than 3.
# You: multiply bigger number with 10 and give me the result
# AI:  Please provide the bigger number.  I need a number to multiply by 10.


