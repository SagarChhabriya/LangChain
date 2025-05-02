from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model="claude-3-5-sonnet-20241022")

result = chat_model.invoke("What is the current rate of US dollar?")

print(result)

