# %%
# imports
import pandas as pd
import openai
from config import CONFIG
from stqdm import stqdm
import streamlit as st

openai.api_key = st.secrets["openai_key"]
excel_file_path = CONFIG["excel_path"]


def extract_answers(questions):
    """
    This function extracts answers from the questions.
    """
    # finding answers for each question
    answer_list = []
    for que in stqdm(questions):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=str(que)
            + """
            Answer:
            """,
            max_tokens=1024,
        )
        answer_list.append(response["choices"][0]["text"].strip())
    return pd.DataFrame(answer_list, columns=["Answers"])


# data = pd.read_excel(excel_file_path)

# finding answers for each question
# answer_list = []
# for que in tqdm(data["Questions"]):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=que+"""
#         Answer:
#         """,
#         max_tokens=1024
#     )
#     answer_list.append(response['choices'][0]['text'].strip())


# # saving the answers to the excel file
# data["Answers"] = answer_list
# data = data[['Questions', 'Answers']]
# data.to_excel(excel_file_path, index=False)
