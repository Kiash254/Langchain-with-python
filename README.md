# Langchain-with-python
LangChain is a framework that uses LLMs to build applications for various use cases.
At a high level, LangChain connects LLM models (such as OpenAI and HuggingFace Hub) to external sources like Google, Wikipedia, Notion, and Wolfram. It provides abstractions (chains and agents) and tools (prompt templates, memory, document loaders, output parsers) to interface between text input and output. LLM models and components are linked into a pipeline "chain," making it easy for developers to rapidly prototype robust applications. Simply put, Langchain orchestrates the LLM pipeline.

LangChain's power lies in its six key modules:

Model I/O: Facilitates the interface of model input (prompts) with the LLM model (closed or open-source) to produce the model output (output parsers)
Data connection: Enables user data to be loaded (document loaders), transformed (document transformers), stored (text embedding models and vector stores) and queried (retrievers)
Memory: Confer chains or agents with the capacity for short-term and long-term memory so that it remembers previous interactions with the user
Chains: A way to combine several components or other chains in a single pipeline (or “chain”)
Agents: Depending on the input, the agent decides on a course of action to take with the available tools/data that it has access to
Callbacks: Functions that are triggered to perform at specific points during the duration of an LLM run

Step 1. Get an OpenAI API key
Go to https://platform.openai.com/account/api-keys.
step 2 : install the requirements
pip install -r requirements.txt
step 3 : deploy the app on streamlit
Deploying the app is super simple:

Create a GitHub repository for the app.
In Streamlit Community Cloud, click the New app button, then specify the repository, branch, and main file path.
Click the Deploy! button.
step 4 : run the app