from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ('system','You are a helpful tutor'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human',"{query}")
])


chat_history = []
# load chat history
with open(r"LangChain\04-prompts\4.5-message-placeholder\chat_history.txt") as file:
    chat_history.extend(file)

print(chat_history)

# create prompt
prompt = chat_template.invoke({"chat_history":chat_history,"query":"what is retrival in RAG?"})