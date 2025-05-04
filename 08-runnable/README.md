# Runnables

The compoenents didn't have a connecting module. To connect each module there were written sepearate chains/code that increased the volume of langchain's codebase. They realized their mistake and proposed a solution. 

Workflow

runnable: unit of work

Unit of work: Input process outptu
Common interface: invoke(), batch(), stream()

consider lago blocks

The ideas was to standardize all the components

Types of Runnables
1. Task Specific
2. Runnable Primitives


### Task Specific
These are core langchain compoenents that have been converted into runnables so they can be used  in pipelines. 
Purpose: Perform task-specific operations like LLM calls, prompting, retrieval, etc.
Ex:
    - ChatOpenAI: Runs an LLM Model
    - PromptTemplate: Formats prompts dynamically
    - Retrievar: retrieves relevant documents.


### Runnable Primitives
These are fundamental building blocks for structuring execution logic in AI workflows. They help orchestrate execution by defining different runnables interact (sequentially, in parallel, conditionally, etc)

Ex:
`Runnable Sequence`: Runs steps in order (| operator)
Runnable Parallel: Runs multiple steps simulatenenously
RunnableMap: Maps the same input across multiple functions.
RunnableBranch: implements conditional execution (if-else logic)
RunnableLambda: wraps custom Python functions into runnables
RunnablePassthrough: Just forwards input as output (acts as a placeholder )



## 1. RunnableSequence
RunnableSequence is a sequential chain of runnables in LangChain that executes each step one after another, passing the output of one step as the input to another.

It is useful when you need to compose multiple runnables together in a structured workflow.


## 2. RunnableParallel
RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel. 

Each runnable receives the same input and processes it independently, producing a dictionary of outputs. 
