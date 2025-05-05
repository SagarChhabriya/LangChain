from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"LangChain\09-document-loaders\9.2-agents.pdf")

docs = loader.load()

print(len(docs)) # 34
print(docs[0].page_content)
print(docs[0].metadata)

# A  p r a c t i c a l  
# g u i d e  t o  
# b u i l d i n g  a g e n t s
# {'producer': 'pdf-lib (https://github.com/Hopding/pdf-lib)', 'creator': 'pdf-lib (https://github.com/Hopding/pdf-lib)', 'creationdate': '2025-04-07T14:20:51+00:00', 'moddate': '2025-04-07T14:20:54+00:00', 'source': 'LangChain\\09-document-loaders\\9.2-agents.pdf', 'total_pages': 34, 'page': 0, 'page_label': '1'}