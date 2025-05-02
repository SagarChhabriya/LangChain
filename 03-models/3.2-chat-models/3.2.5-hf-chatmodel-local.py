from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# My C Drive is don't have enough space that is the default location when model is downloaded
import os 
os.environ['HF_HOME'] = "D:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100)
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Prime Minister of Pakistan?")

print(response.content)