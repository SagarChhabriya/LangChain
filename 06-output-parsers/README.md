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

### JSON OutputParser
Its dictionary like object.

```bash
    key:[
        value1,
        value2,
        ...
        value_n
    ]
```


It doesn't enforce a schema. for example:

```bash
    {
    fact1: value1,
    fact2: value2,
    ...
    fact_n:value_n
    }
```

The solution is StructuredOutputParser

### StructuredOutputParser
StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.


It workds by defining a list of field (ResponseSchema) that the model should return, ensuring the output follows a structured format. 

It doesn't support data validation.

The solution is Pydantic Output Parser.

### Pydantic Output Parser
`PydanticOutputParser` is a structured output parser in LangChain that uses `Pydantic models` to enforce schema validation when processing LLM responses. 