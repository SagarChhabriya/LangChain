# Paid
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model="claude-3-sonnet-20240229")

result = chat_model.invoke("What is the current rate of US dollar?")

print(result)

