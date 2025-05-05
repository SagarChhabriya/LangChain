from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os 

load_dotenv()

# Step 1: Load the document

# Get the folder where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full path to the text file
file_path = os.path.join(base_dir, "9.1-corpus.txt")

# loader = TextLoader(r"D:\Ao\Code\GenAI\LangChain\09-document-loaders\9.1-corpus.txt", encoding="utf-8")
loader = TextLoader(file_path)
docs = loader.load()

print("docs type: ", type(docs)) # list of langchain documents | docs type:  <class 'list'>
print("doc type: ", type(docs[0])) # doc type:  <class 'langchain_core.documents.base.Document'>
print("docs length: ", len(docs)) # docs length:  1
print("first doc docs[0] : ", docs[0])
print("page_content : ", docs[0].page_content)
print("metadata : ", docs[0].metadata)
print("-"*55)



# Step 2: Prompt
prompt = PromptTemplate(
    template="Write a summary of the following: \n{text}",
    input_variables=["text"]
)



# Step 3: Model 
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro") 

# Step 4: Parser
parser = StrOutputParser()

# Step 5: Chain
chain = prompt | chat_model | parser

result = chain.invoke({"text":docs[0].page_content})

print(result)

