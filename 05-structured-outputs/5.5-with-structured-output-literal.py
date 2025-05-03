
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")


class Review(TypedDict):
    key_themes: Annotated(list[str], "Write down all the key themes discussed in review.")
    summary:Annotated(str,"A brief summary of the reivew")
    sentiment:Annotated(Literal["pos","neg"],"Return sentiment of the reivew e.g., negative, positive, or neutral")
    # pros & cons are made optional
    pros: Annotated(Optional[list[str]], "Write down all the pros inside a list.")
    cons: Annotated(Optional[list[str]], "Write down all the cons inside a list.")
    
struc_chat_model = chat_model.with_structured_output(Review)

result = struc_chat_model.invoke("""The hardware is great, but the software feels bloated. 
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated 
compared to other brands. Hoping for a software update to fix this.
""")

print(result)