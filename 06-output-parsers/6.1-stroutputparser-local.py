# Without Chains
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# LLM setup
llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    repo_id="google/gemma-2-2b-it", # 17.5 MB File
    task="text-generation",
)
model = ChatHuggingFace(llm=llm)

# Prompt templates
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text:\n{text}',
    input_variables=['text']
)

# Invoke detailed report
prompt1 = template1.invoke({'topic': 'black hole'})
report = model.invoke(prompt1)
print("Detailed Report:\n", report)

# Invoke summary
prompt2 = template2.invoke({'text': report.content if hasattr(report, "content") else report})
summary = model.invoke(prompt2)
print("\n5-Line Summary:\n", summary.content if hasattr(summary, "content") else summary)
