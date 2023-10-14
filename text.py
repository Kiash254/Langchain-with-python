from langchain.llms import OpenAI
import streamlit as st

OPENAI_API_KEY=os.environ.get("API_KEY")

def main():
  llm=OpenAI(openai_api_key=OPENAI_API_KEY)
  result=llm.generate(
      text='Give 5 topics for intresting Youtube Vedioes',
      max_tokens=50
  )
  
  st.write(result)


if __name__=="__main__":
  main()