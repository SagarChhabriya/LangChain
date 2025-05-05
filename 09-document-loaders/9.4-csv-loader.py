from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r"LangChain\09-document-loaders\cgpa.csv")
docs = loader.load()

print(len(docs))
print(docs[0])