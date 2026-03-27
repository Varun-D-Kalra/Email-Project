# This is my first exposure to UI with streamlit.
# This file will have a box to accept copied email and return the summary.

import streamlit as st

st.header("Welcome To Email Intelligence")
st.subheader("Summarised Output")

st.text_input("Paste your Email here!")

st.button("PROCESS")

# Print output from the summary after further cleaning