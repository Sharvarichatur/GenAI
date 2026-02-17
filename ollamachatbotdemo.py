import os
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM

prompt = ChatPromptTemplate.from_messages(
    [
        # System message defines AI behavior
        ("system", "You are a helpful assistant. Please respond clearly to the question asked."),
        
        # User message contains placeholder {question}
        ("user", "Question: {question}")
    ]
)
# App Title
st.title("LangChain Demo with Gemma Model (Ollama)")

# Text input box for user question
input_text = st.text_input("What question do you have in mind?")


# Load local Gemma model (must be pulled using Ollama)
llm = Ollama(model="gemma2:2b")

# Convert model output to string
output_parser = StrOutputParser()

# Create LangChain pipeline (Prompt → Model → Output Parser)
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)



