import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
OPENAI_API_KEY=os.environ.get("API_KEY")

def main():
  llm=OpenAI(openai_api_key=OPENAI_API_KEY)
  result=llm.generate(
      text='Give 5 topics for intresting Youtube Vedioes',
      max_tokens=50
  )
  
  print(result)


if __name__=="__main__":
  main()