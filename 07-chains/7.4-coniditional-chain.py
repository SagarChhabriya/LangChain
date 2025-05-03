from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableBranch, RunnableParallel, RunnableLambda

load_dotenv()


# Step 1: Parsers

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")


parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)


# Step 2: Prompts

# Prompt 1: Prompt for Classification/Analysis
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions":parser2.get_format_instructions()}
)

# Prompt 2: Prompt for Positive
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"],
)

# Prompt 3: Prompt for Negative
prompt3 = PromptTemplate(
    template="Write an appropriate to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

# Step 3: Model 
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")



# Step 4: Chains

classifier_chain = prompt1 | chat_model | parser2

branch_chain = RunnableBranch(
    # (condition, chain)
    # ...
    # (condition, chain)
    # defualt chain
    (lambda x: x.sentiment == "positive", prompt2 | chat_model | parser1),
    (lambda x: x.sentiment == "negative", prompt3 | chat_model | parser1),
    # lambda x: "couldn't fint sentiment" # but we need to have a chain in defualt statement and it can't be empty.abs
    RunnableLambda(lambda x: "coudn't find sentiment")
)


chain = classifier_chain | branch_chain
print(chain.invoke({"feedback":"We won the match"}))



