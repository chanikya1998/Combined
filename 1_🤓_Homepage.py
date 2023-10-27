import streamlit as st

st.set_page_config(
    page_title="Med-Kick Dashboard App",
    page_icon="👋",
)

image_path = "medkicklogo.png"
st.title("Med-Kick Dashboards")

st.image(image_path, caption="", use_column_width=True)
st.sidebar.success("Select a page above.")
