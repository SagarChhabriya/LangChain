from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


class Review(TypedDict):
    summary:Annotated(str,"A brief summary of the reivew")
    sentiment:Annotated(str,"Return sentiment of the reivew e.g., negative, positive, or neutral")

struc_chat_model = chat_model.with_structured_output(Review)

result = struc_chat_model.invoke("""The hardware is great, but the software feels bloated. 
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated 
compared to other brands. Hoping for a software update to fix this.
""")

print(result)

