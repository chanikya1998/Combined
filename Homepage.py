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

# Define allowed users and their passwords (replace with your own data)
allowed_users = {
    "user1": "password1",
    "user2": "password2",
    # Add more users as needed
}

# Initialize the Streamlit Authenticator
authenticator = stauth.Authenticator(allowed_users)

# Check if the user is authenticated
if not authenticator.authenticate():
    st.error("Authentication failed. Please check your credentials.")
    st.stop()

# Your Streamlit app code goes here
# This code will only be executed if the user is authenticated
# You can add your app's functionality below this point