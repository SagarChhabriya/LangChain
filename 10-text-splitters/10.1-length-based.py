from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter

loader = TextLoader(r"D:\Ao\Code\GenAI\LangChain\10-text-splitters\10.1-corpus.txt")
docs = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)
print(result[1].page_content)


