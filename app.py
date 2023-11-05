from langchain.llms import OpenAI
from dotenv import load_dotenv
import os 
import streamlit as st

os.environ.get("OPENAI_API_KEY")  # this function will load all the nessecisary key

## create a function that load the openAI model and get responses

def get_openAI_response(question):
    llm = OpenAI(model_name="text-davinci-003", temperature= 0.6)
    response = llm(question)
    return response

## initialize the strealit app 
st.set_page_config(page_title="Q&A Demo")
st.header("langchain Application")
input = st.text_input('Input: ', key='input')
response = get_openAI_response(input)
submit = st.button('Ask the Question')


if submit:
    st.subheader("the respnse is ")
    st.write(response)




