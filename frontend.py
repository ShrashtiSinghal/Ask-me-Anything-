# %%
# using streamlit to build frontend
# IMPORTS
import streamlit as st
import pandas as pd
import numpy
from st_aggrid import AgGrid, GridOptionsBuilder
from extract_answer import *

# DEFAULTS
st.set_page_config(
    layout="wide",
    page_title="Ask me anything",
    page_icon="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/72x72/2753.png",
)
title = st.title("Ask me Anything! ")

# UPLOAD INTERFACE
excel_file = st.file_uploader("Upload your excel file", type=["xlsx", "xls", "csv"])
st.caption("csv, xlsx, xls files are supported")


# %%
# for downloading the output
@st.experimental_memo
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8")


# EXTRACTING ANSWERS
if excel_file is not None:
    # selecting the question columns
    if excel_file.name.endswith(".csv"):
        excel_file = pd.read_csv(excel_file)
    else:
        excel_file = pd.read_excel(excel_file)
    question_col = st.selectbox(
        "Select the column containing questions", excel_file.columns
    )
    # button for finding answers
    output = None
    but = st.button("Find answers")
    if but:
        answer_df = extract_answers(excel_file[question_col])
        st.success("Answers found")

        # final output
        output = pd.DataFrame()
        output["Questions"] = excel_file[question_col]
        output["Answers"] = answer_df["Answers"]
        csv = convert_df(output)

    if output is not None:
        # displaying the output
        AgGrid(output, wrapText=True, fit_columns_on_grid_load=True)
        st.download_button(
            "Press to Download", csv, "Output.csv", "text/csv", key="download-csv"
        )
