from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age, and city of a fictional person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
    
)

# Approach 1:

prompt = template.format()

print(prompt)

# Output:
# Give me the name, age, and city of a fictional person 
#  Return a JSON object.

print(chat_model.invoke(prompt))

# Output:

# content='```json\n{\n  "name": "Evelyn Reed",\n  "age": 37,\n  "city": "Port Blossom"\n}\n```' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'model_name': 'gemini-1.5-pro-002', 'safety_ratings': []} id='run-d799bc67-7c69-4356-812a-4995016aff36-0' usage_metadata={'input_tokens': 20, 'output_tokens': 36, 'total_tokens': 56, 'input_token_details': {'cache_read': 0}}


# Approach 2:
chain = template | chat_model | parser
result  = chain.invoke()
print(result)
