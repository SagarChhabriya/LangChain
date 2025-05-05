from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

# Step 1: Load data from url
url = "https://github.com/SagarChhabriya"
loader = WebBaseLoader(url)
docs = loader.load()

# Step 2: Prompt
prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=["question","text"]
)

# Step 3: model 
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Step 4: Output Parser
parser = StrOutputParser()

# Step 5: Chain
chain = prompt | chat_model | parser

result = chain.invoke({"question":"What is the name of user? What does it's profile says?","text":docs[0].page_content})
print(result)

# Output:
# The user's name is Sagar Chhabriya (SagarChhabriya on GitHub).  Their profile states they are a GenAI Engineer currently on vacation. They are interested in Machine Learning, AI, Data Science, Data Structures, and Python, and are currently learning Deep Learning and GenAI.  They list their location as Pakistan and link to their LinkedIn, Stack Overflow, and Medium profiles.  They also include a list of projects they've worked on, categorized by AI & Machine Learning, Data Applications, Python, and Java Applications.  Their profile also mentions they passed the GitHub Foundations Exam.