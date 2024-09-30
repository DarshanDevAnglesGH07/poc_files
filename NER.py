import os
import streamlit as st
st.write("Current working directory:", os.getcwd())
st.write("Contents of /app directory:", os.listdir("/app"))
