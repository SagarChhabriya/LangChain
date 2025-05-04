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

## 3. RunnablePassthrough
RunnablePassthrough is a special runnable primitive that simply returns the input as output without modifying it. 

Consider a scenario in `SequentialRunnable` having prompt1 `write down a joke` and prompt2 `write down the explanation of joke`. You will get the the explanation of joke but the joke wasn't printed. It means you only get the result of last prompt only. But what if I need the output of all prompts i.e., the joke with its explanation. This situation can be handled by RunnablePassthrough. 


## 4. RunnableLambda
RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline. 

It acts as a middleware between deifferent AI components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflow. 

## 5. RunnableBranch (Conditional Chains)
RunnableBranch is a flow control component in LangChain that allows you to conditionally route input data to different chains or runnables based on custom logic.

It functions like an if/elif/else block for chains, where you define the set of condition functions, each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed. If no condition matches a default runnable is used (if provided).


## LCEL (LangChain Expression Language)
LangChain Expression Language (LCEL) is a syntax in LangChain that simplifies composing complex LLM chains and workflows. It allows developers to represent complex workflows with minimal code, offering features like parallel execution, streaming, and asynchronous support. 

LCEL uses a declarative approach, meaning you define what you want to happen rather than how. LangChain then optimizes the execution of these chains at runtime. 

LCEL utilizes a pipe operator (|) to connect different LangChain components in a sequence.


### 1. Component Integration
Use LCEL to link LLMs, prompts, and output parsers.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Translate to French: {text}")
llm = ChatOpenAI()
parser = StrOutputParser()

chain = prompt | llm | parser
chain.invoke({"text": "Hello, how are you?"})
```

### 2. Stream and Async Support

Supports async and streaming by default.

```python
# Async
response = await chain.ainvoke({"text": "Good morning"})

# Streaming
async for chunk in chain.astream({"text": "Stream this"}):
    print(chunk, end="")
```

### 3. Parallelization

Run multiple chains at the same time.

```python
from langchain_core.runnables import RunnableParallel

chain1 = prompt | ChatOpenAI(model="gpt-3.5-turbo") | parser
chain2 = prompt | ChatOpenAI(model="gpt-4") | parser

parallel_chain = RunnableParallel(model1=chain1, model2=chain2)
parallel_chain.invoke({"text": "What is the capital of France?"})
```

### 4. Flexibility and Composability

Modify or reuse parts of the chain easily.

```python
# Reuse the prompt with different parsers or models
new_chain = prompt | ChatOpenAI() | StrOutputParser()
```

### 5. Unified Interface

All chains use the same interface methods.

```python
chain.invoke({"text": "Thanks"})         # Synchronous
await chain.ainvoke({"text": "Async"})   # Asynchronous
```
