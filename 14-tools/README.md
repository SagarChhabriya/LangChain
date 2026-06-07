# Tools
A tool is just a python function (or API) that is packaged in a way the LLM can understand and call when needed. 

LLMs like GPT are great at:
- Reasoning
- Language Generation

But they can't do things like: 
- Access live data (weather, news)
- Do reliable math
- Call APIs
- Run Code
- Interact with a database

- **Tools in LangChain**
    - Built-in
    - Custom

### How tools fits into Agent Ecosystem
An AI agent is an LLM powered system that can autonomously think, decide, and take actions using external tools or APIs to achive goal. 


## Built-in Tools
LangChain provided production ready and requires minimal or no setup. 
You don't have to write the function logic yourself, you just import it and use it. 

| Tool | Description |
|------|-------------|
|DuckDuckGoSearchRun| Web search via DuckDuckGo|
|WikipediaQueryRun|Wikipedia Summary|
|PythonREPLTool|Run raw python code|
|ShellTool|Run shell commands|
|RequestGetTool|Make HTTP GET requests|
|GmailSendMessageTool|Send emails via Gmail|
|SlackSendMessageTool|Post message to slack|
|SQLDatabaseQueryTool|Run SQL queries | 


## Custom Tools
User defined tool. When you want:
- to call your own APIs
- to encapsulate business logic
- the LLM to interact with your database, product, or app. 

1. Using @tool decorate
2. Using StructuredTool & Pydantic
3. Using BaseTool class

- **Structured Tool**
A structured tool in LangChain is a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model. 

- **BaseTool**
An abstract base class for all tools in LangChain. It defines the core structure and interface that any tool must follow, whether it's a simple one-linear or a fully customized function. 

All other tool types like `@tool`, `StructuredTool` are built on top of BaseTool. 


## Toolkits
A toolkit is just a collection of related tools that serve a common purpose, packaged together for convenience and reusability. 

In LangChain:
- A toolkit might be: GoogleDriveToolkit
- And it can contain the following tools
    - GoogleDriveCreateFileTool: Upload a File
    - GoogleDriveSearchTool: Search for a file by name/content
    - GoogleDriveReadFileTool: Read contents of a file



## Tool Binding
Tool binding is the step where you register tools with a LLM so that:
1. The LLM knows what tools are available
2. It knows what each tool does (via description)
3. It knows what input for to use (via schema)

## Tool Calling
Tool calling is the process where the LLM decides, during a conversation or task, that it needs to use a specific tool (function) and generates a structured output with:
- the name of the tool
- and the arguments to call it with 

The LLM doesn't actually run the tool, it just suggests the tool and the input arguments. The actual execution is handled by LangChain or you. 


## Tool Execution
The tool execution is the step where the actual Python function (tool) is run using the input arguments that the LLM suggested during tool calling. 