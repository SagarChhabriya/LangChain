# Output Parsers
Output Parsers in LangChain help convert RAW LLM responses into structured formats like JSON, CSV, Pydantic models and many more. They ensure consistency, validation, and ease of use in applications. 

By default the OpenAI, Anthropic, gemini or some other paid models support the structured output in most of the cases. But most of the open-source models doesn't support the structured output by default. 

- **Four most common output parsers**
    - StrOutputParser
    - JSONOutputParser
    - StructuredOutputParser
    - PydanticOutputParser


### StrOutputParser
The StrOutputParser is the simplest output parser in LangChain. It is used to parse the output of a Language Model (LLM) and returns it as a plain string.