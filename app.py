
import sys
from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="Streamlit Deployment Test",
    page_icon="🧪",
    layout="centered"
)

st.title("Streamlit Deployment Test")

st.success("Your Streamlit application is running successfully!")

st.subheader("Environment Information")

st.write("Python Version:", sys.version.split()[0])
st.write("Streamlit Version:", st.__version__)
st.write("Server Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

st.subheader("Interactive Test")

name = st.text_input("Enter your name")

if st.button("Test Application"):
    if name.strip():
        st.success(f"Hello, {name}! Your application is responding.")
    else:
        st.warning("Please enter your name.")

st.subheader("Chart Test")

st.line_chart([12, 18, 15, 24, 21, 30])

st.info("If you can see this page, your Streamlit deployment is working.")
