import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

# User data (names, usernames, and hashed passwords)
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]
# In practice, you should securely store hashed passwords.
# For this example, we'll use plain text passwords for simplicity.
hashed_passwords = {
    "pparker": "password1",
    "rmiller": "password2"
}

# Initialize the Streamlit app
st.set_page_config(
    page_title="Med-Kick Dashboard App",
    page_icon="👋",
)

# Create an instance of the authenticator
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, cookie_expiry_days=30)

# Login and authentication status
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status is False:
    st.error("Username/password is incorrect")

if authentication_status is None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.title("Med-Kick Dashboard App")
    image_path = "medkicklogo.png"
    st.image(image_path, caption="", use_column_width=True)
    st.sidebar.success("Select a page above.")

    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
    """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # Now, you can add your dashboard content here for authenticated users.
    # For example, you can display financial charts or reports.
    # Modify the code within this block to suit your dashboard's needs.

    # Example: Display a chart
    st.subheader("Financial Dashboard")
    st.write("Your financial charts go here.")
