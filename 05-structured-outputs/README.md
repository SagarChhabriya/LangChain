# Structured Outputs

By default the output is unstructured which is nothing but text.
In LangChain, structured output refers to the practice of having language models return responses in a well-defined data format (e.g., JSON) rather than free-form text. This makes the model output easier to parse and work with programmatically.

- `Prompt` - _Can you create a one day travel plan for paris?_
- `LLMs' Unstructured Response`:

```bash
Here's suggested plan: Morning: Visit the Eiffel Tower.
Afternoon: Walk through the Louvre Museum.
Evening: Enjoy dinner at a Seine riverside cafe.
```
- `JSON enforced output`:

```bash
[
    {"time":"Morning", "activity":"Visit the Eiffel Tower"},
    {"time":"Afternoon","activity":"Walk through the Louvre Museum"},
    {"time":"Evening","activity":"Enjoy dinner at a Seine riverside cafe"}
]
```

### Why do we need Structured Output?
- Data Extraction
Let's suppose we are building an app that extract the candidates' data from their resume:
    - Step 1: Extract the data
    - Step 2: Feed the data to LLM and get result in JSON
    - Step 3: Store the results in a database
- API building
Bulding a review analyzer for amazon like companies:
    - Extract the: topic, pros, cons, sentiment from the review (text input).
    - Build an API and give access to the results
- Agents
Agents need tools to perform tasks. Consider a query `Find the multiplication of 2 and 5`, we can't send the query to a tool like calculator in the given form rather we need to convert it into a JSON like format and then send it to the calculator like tool. These tools can't work with textual data.


### Ways to get Structured Output
1. With Structured Output
LLMs with built-in capability of generating structured output.
2. Without Structured Output
LLMs without built-in capability of generating structured output. This can be solved using output parsers of langchain.

In this module we'll be focusing on the first type `with_structured_output` generating, and in the next module we'll dicuss the output parsers. Usually we call the invoke method to generate the response, just before that we have to call the with_structure_output by specifying the data_format to get the structured output.

- **Three most common ways of format**:
    - TypedDict
    - Pydantic
    - json_schema


## TypedDict
TypedDict is a way to define a dictionary in Python where you specify what keys and vlaues should exist. It helps ensure that your dictionary follows a specific structure.

- **Why use TypedDict**
    - It tells Python what keys are required and what types of values they should have. It won't generate an error if you pass an string to a integer type variable.
    - It does not validate at runtime (it just helps with type hints for better coding).

- **Types of TypedDict**
    - Single TypedDict
    - Automated TypedDict
    - Literal
    - More Complex: With pros and cons

The issue with TypedDict is we can't have the validation rather it's just a representation technique. It means, you explicitly specifying the types of keys such as str for summary, sentiment, etc but there is no gaurantee that the LLM will always returns the reponse in str. So there comes the `Pydantic`.

## Pydantic
Pydantic is a data validation and data parsing library for Python. It ensures that the data you work with is correct, structured, and type-safe.

- **Agends**
    - Basic Example
    - Default values
    - Optional Fields
    - Type Coerce (implicitly)
    - Built-in validation
    - Field Functions: default values, constraints, description, regex
    - Expressions
    - Returns pydantic object: convert to json/dict


## JSON Schema
Sometimes developers design the frontend using JS and backed using Python in such cases the typedDict and Pydantic doesn't support. JSON Schema is a way to deal with such scenarios.