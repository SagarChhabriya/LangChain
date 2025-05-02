from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32) # default 15xx

docs = [
    "My Name is Sagar Chhabriya",
    "I'm from Sindh Pakistan",
    "Every problem has a unique solution 😊"
]

response = embeddings.embed_documents(docs)

print(str(response))