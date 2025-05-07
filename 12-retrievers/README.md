# Retrievers
A retriever is a componenet in LangChain that fetches relevant documents from a data in repsonse to a user's query.

There are multiple types of retrievers and all retrievers in LangChain are runnables. 

## Wikipedia Retriever
A Wikipedia retriever is a retriever that queries the Wikipedia API to fetch relevant content for a given query.

- **How it works**
1. You give it a query (e.g., Computer Science)
2. It send the query to Wikipedia's API 
3. It retrieves the most relevant articles
4. It returns them as LangChain `Document` object


## Vector Store Retriever
A vector store retriever in LangChain is the most common type of retriever that lets you search and fetch documents from a vector based on semantic similarity using vector embeddings. 

- **How it works**
1. You store your documents in a vector store (like FAISS, Chroma, Weaviate) 
2. Each document is converted into a dense-vector using an embedding model
3. When the user enters a query
    - It's also turned into a vector 
    - The retriever compares the query vector with the stored vectors
    - it retrieves the top-k most similar ones. 


## Maximal Marginal Relevance (MMR)
MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved result while maintaining high relevance to the query.

`How can we pick results that are not only relevant to the query but also different from each other?`

In regular similarity search, you may get documents that are:
    - All very similar to each other
    - repeating the same info
    - Lacking diverse perspectives

MMR Retriever avoids that by:
    - Picking the most relevant document first
    - Then picking the next most relevant and least similar to already selected docs


## Multi Query Retriever
Sometimes a single query might not capture all the ways information is phrased in your documents.

Query: How can I stay health?

Could means:
    - What should I eat?
    - How often should I exercise?
    - How can I manage stress?

A simple similarity search might miss documents that talk about those things but don't use the word healthy.

- **How it works**
    - Takes your original query
    - User an LLM (e.g., Gemini, GPT-4) to generate multiple semantically different versions of that query 
    - Performs retrieval for each sub-query
    - Combines and deduplications the results


## Contextual Compression Retriever
The Contextual compression retriever in LangChain is an advanced retriver that improves retrieval quality by compressing documents after retrieval, keeping only the relevant content based on the user's query.

- **Working Rule**
    - Base Retriever (e.g., FAISS, Chroma) retrieves N documents.
    - A compressor (usually an LLM) is applied to each document.
    - The compressor keeps only the parts relevant to the query.
    - Irrelevant content is discarded.

- **Usage**
    - When your documents are long and contain mixed information
    - You want to reduce context lenght for LLMs.
    - You need to improve answer accuracy in RAG Pipelines. 

## More Retrievers (Advance RAG: To improve Traditional RAG)
- BM25Retriever
- ParentDocumentRetriever
- SelfQueryRetriever
- TimeWeightedRetriever
- MultiVectorRetriver
- EnsembleRetriever
- ArxivRetriever

