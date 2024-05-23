import os
import traceback
import pandas as pd
import json

from src.utils import read_file,get_table_data
from src.logger import logging

#importing necessary packages from langchain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback

#load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

#access the environment variable
KEY=os.getenv('OPENAI_API_KEY')

llm_model=OpenAI(openai_api_key=KEY,model_name="gpt-3.5-turbo",temperature=0.7)

TEMPLATE1='''
Text:{text}
You are an expert MCQ maker. Given the above text it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be confirming the text as well.
Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs
### RESPONSE_JSON
{response_json}
'''

quiz_generation_prompt = PromptTemplate(
    input_variables=['text','number','subject','tone','response_json'],
    template=TEMPLATE1
)

quiz_chain=LLMChain(llm=llm_model,prompt=quiz_generation_prompt,output_key='quiz',verbose=True)

TEMPLATE2 = '''
You are an expert english grammarian and writer.Given a multiple choice quiz for {subject} students. \
you need to evluate the complexity of the question and give a complete analysis of the quiz.
Only use at max 50 words for complexity .
If the quiz is not at per with the cognitive and analytical abilities of the students, \
update the quiz questions which need to be changed and change the tone so that it perfectly fits the student abilities.
Quiz_MCQs:
{quiz}

Check from an expert english writer of the above quiz.
'''

quiz_evaluation_prompt = PromptTemplate(
    input_variables=['subject','quiz'],
    template=TEMPLATE2
)

review_chain=LLMChain(llm=llm_model,prompt=quiz_evaluation_prompt,output_key='review',verbose=True)

#this is an overall chain where we run the two chains in sequence
generate_evaluate_chain=SequentialChain(chains=[quiz_chain,review_chain],input_variables=['text','number','subject','tone','response_json'],
                        output_variables=['quiz','review'],verbose=True)