# TextSplitters
Text splitting is the process of breaking large chunks of text (like articles, PDFs, HTML Pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively. 

- **Overcoming model limitation**: Many embedding models and language models that have maximum input size constraints. Splitting allows us to process documents, otherwise exceed these limits. 

- **Downstream tasks**: Text splitting improves nearly every LLM powered task

| Task | Why Splitting Helps |
|------|---------------------|
|Embedding | Sort chunks yield more accurate vectors|
|Semantic Serach | Search results point to focused info not noise|
|Summarization| Prevents hallucination and topic drift |

- **Optimizing computational resources**: Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks. 

![](../assets/9.2-text-splitters.png)

![Tool: https://chunkviz.up.railway.app/](https://chunkviz.up.railway.app/)



### 1. Length-Based Splitting
- **What**: Divides text after fixed character/token counts
- **Best for**: Uniform documents where structure matters less
- **Example**: 
  ```python
  # Splitting every 500 characters
  text = "Your long document..."
  chunks = [text[i:i+500] for i in range(0, len(text), 500)]
  ```
- **Pros**: Simple to implement, consistent chunk sizes
- **Cons**: Often breaks sentences/ideas mid-flow

### 2. Text Structure-Based Splitting
- **What**: Uses natural delimiters in the text
- **Best for**: Well-formatted content (Markdown, code, etc.)
- **Delimiters**:
  - `\n\n` - Paragraph breaks
  - `\n` - Line breaks
  - Headers (`#`, `##`) - Section boundaries
- **Example** (Markdown):
  ```python
  chunks = text.split("\n\n")  # Split by paragraphs
  ```
- **Pros**: Preserves logical groupings
- **Cons**: Requires consistent formatting

### 3. Document Structure-Based Splitting
- **What**: Leverages file format hierarchy
- **Best for**: PDFs, HTML, Word docs, presentations
- **Elements**:
  - PDF: Pages, sections, headings
  - HTML: `<div>`, `<p>`, `<h1>` tags
  - Word: Headers, footers, tables
- **Tools**:
  - `PyPDF2` (PDFs)
  - `BeautifulSoup` (HTML)
  - `python-docx` (Word)
- **Pros**: Maintains document semantics
- **Cons**: Parser-dependent, format-specific

### 4. Semantic Meaning-Based Splitting
- **What**: Splits at natural idea boundaries
- **Best for**: Research papers, complex reports
- **Methods**:
  - Sentence transformers
  - Topic modeling
  - LLM-assisted splitting
- **Example** (using NLTK):
  ```python
  from nltk.tokenize import sent_tokenize
  chunks = sent_tokenize(text)  # Split by sentences
  ```
- **Pros**: Preserves complete thoughts
- **Cons**: Computationally intensive

### Comparison Table

| Technique          | Speed  | Accuracy | Best Use Case               |
|--------------------|--------|----------|-----------------------------|
| Length-Based       | Fast   | Low      | Quick preprocessing         |
| Structure-Based    | Medium | Medium   | Formatted docs (Markdown)   |
| Document-Based     | Slow   | High     | PDFs/HTML/Office docs       |
| Semantic-Based     | Slowest| Highest  | Critical analysis tasks     |

**Pro Tip**: For RAG applications, combine structure-based initial splitting with semantic-based refinement for optimal results.