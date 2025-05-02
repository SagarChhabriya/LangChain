from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Hugging Face token from environment variable
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Create an endpoint with the token
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    huggingfacehub_api_token=hf_token
)

# Wrap it in a chat model
model = ChatHuggingFace(llm=llm)

# Invoke the model
response = model.invoke("What is the capital of pakistan?")
print(response.content)

