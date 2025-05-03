from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} assistant'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({"domain":"RAG","topic":"Vector DB"})

print(prompt)