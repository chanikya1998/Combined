import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

# Initialize the Streamlit app
st.set_page_config(
    page_title="Med-Kick Dashboard App",
    page_icon="👋",
)

st.title("Financial Dashboards")
image_path = "medkicklogo.png"
st.image(image_path, caption="", use_column_width=True)
st.sidebar.success("Select a page above.")
