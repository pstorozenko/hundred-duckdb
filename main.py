import streamlit as st
import pandas as pd
import requests
import duckdb


fastapi_url = "http://localhost:8000/add_answer/"
con = duckdb.connect("data.sqlite", read_only=True)

st.title("Concurrent answers table from duckdb")

"## Statistics of answers from all users"

df = con.sql("SELECT answer FROM ANSWERS").df()
df_processed = df['answer'].str.capitalize().value_counts()
"Users' favorite dish"
st.write(df_processed)

"## Add your dish!"

favorite_dish = st.text_input("My favorite dish")
if st.button("Submit answer"):
    if len(favorite_dish) == 0:
        st.info("Input dish first!")
    else:
        answer = {"answer": favorite_dish.lower()}
        response = requests.post(fastapi_url, json=answer)
        if response.status_code == 200:
            st.info("Response added!")
            st.experimental_rerun()
        else:
            st.error("Some error :(")
