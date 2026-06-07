# RAG
RAG is a way to make a language model (like ChatGPT) smarter by giving extra information at the time you ask your questions. 


LLM --> Fine Tuning --> In Context Learning --> RAG

RAG (Retrieval-Augmented Generation) addresses key challenges such as:

- **Private data access**: By retrieving relevant information from secure, proprietary sources without exposing it to the model directly.
- **Recent developments**: By incorporating up-to-date external content beyond the model's training data.
- **Hallucinations**: By grounding responses in factual, retrieved context to improve accuracy and reduce misinformation.




RAG is consist of:
- Indexing
- Retrieving
- Augmentation
- Generation


## Indexing
The process of preparing your knowledge base so that it can be efficiently searched at query time. This step is consist of 4 sub-steps.

1. Document Ingestion 
Load the source knoeledge into memory.

- PDF Reports, Word Documents
- YouTube Transcripts, blog pages
- GitHub Repos, internal wikis
- SQL Records, Scraped WebPages
- Tools:
    - LangChain Loaders {PyPDFLoader, YouTubeLoader, WebBaseLoader, GitLoader, etc}

2. Text Chunking
Break large documents into small, semantically meaningful chunks. 

- Why Chunks?
    - LLMs have context limits (e.g.,   4k-100k tokens)
    - Smaller Chunks more focused and better semnatic serach
    - Tools:
        - RecursiveCharacterLoader, MarkdownHeaderTextSplitter, SemnaticChunker

3. Embedding Generation
Convert each chunk into a dense vector (embedding) that captures its meaning.

- Why embeddings?
    - Similar ideas land close in vector space.
    - Allows fast fuzzy semantic search.
    - Tools:
        - OpenAIEMbeddings, SentenceTransformerEmbeddings, InstructorEmbeddings, etc. 

4. Vector Store
Store the vectors along with original chunk text and metadata in a vector database.

- VectorDBOptions
    - Local: FAISS, Chroma
    - Cloud: PineChone, Weaviate, Milvus, Qdrant

## Retrieval
The real-time process of finding the most relevant peices of information from a pre-built index(created during indexing) based on the user's question. 

## Augmentation 
The step where the retrieved documents (chunks of relevant context) are combined with the user's query to form a new, enrchied prompt for the LLM.


## Generation
The final step involves the large language model (LLM) using the user query along with the retrieved context to generate a contextually informed response.


## Improvements
1. Evaluation
    - Ragas
    - LangSmith

2. Indexing
    - Document Ingestion
    - Text Splitting
    - Vector Store
3. Retrieval 
    - Pre-retrieval 
        - Query rewriting using LLM
        - Multi-query generation
        - Domain aware routing
    - During Retrieval
        - MMR
        - Hybrid Retrieval
        - Reranking
    - Post-retrieval
        - Contextual Compresion
4. Augmentation 
    - Prompt Templating
    - Answer Grounding
    - Context Window Optimization
5. Generation
    - Answer with Citation
    - Gaurd railing
6. System Design
    - Multimodal
    - Agentic
    - Memory based