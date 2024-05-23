import os
import traceback
import pandas as pd
import json
import streamlit as st

from src.utils import read_file,get_table_data
from src.logger import logging
from src.mcqgenerator.mcq_gen import generate_evaluate_chain

from langchain.callbacks import get_openai_callback

#loading json file
with open('F:\MCQ-Generator\Response.json','r') as file_obj:
    RESPONSE_JSON=json.load(file_obj)

#creating a title for the app
st.title("MCQ Creating Application with Langchain")

#creating a form
with st.form("user_inputs"):
    #file upload
    uploaded_file=st.file_uploader("Upload a pdf or txt file")

    #number of MCQs
    mcq_count = st.number_input("No. of MCQs ",min_value=3,max_value=20)

    #subject
    subject=st.text_input("Give the name of your subject/topic",max_chars=50)

    #quiz tone
    quiz_tone=st.text_input("complexity level of questions",max_chars=20,placeholder="simple")

    #add button
    button=st.form_submit_button("Create MCQs")

    #check if the button is clicked and all fields have input 

    if button and uploaded_file is not None and mcq_count and subject and quiz_tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)

                #count tokens and the cost of API call
                # setting up token usage tracking in langchain
                with get_openai_callback() as cb:
                    response=generate_evaluate_chain(
                        {
                            'text':text,
                            'number': mcq_count,
                            'subject': subject,
                            'tone': quiz_tone,
                            'response_json': json.dumps(RESPONSE_JSON)
                        }
                    )
            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")

            else:
                print(f"total tokens : {cb.total_tokens}")
                print(f"prompt tokens : {cb.prompt_tokens}")
                print(f"completion tokens : {cb.completion_tokens}")
                print(f"total cost : {cb.total_cost}")

                if isinstance(response,dict):
                    #extract the quiz data prom the response
                    quiz=response.get('quiz',None)
                    if quiz is not None:
                        quiz_table_data=get_table_data(quiz)
                        if quiz_table_data is not None:
                            df=pd.DataFrame(quiz_table_data)
                            df.index=df.index+1
                            st.table(df)

                            #displaying the review in a text box
                            st.text_area(label="Review", value=response["review"])

                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)