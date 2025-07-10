import streamlit as st
from info import full_name, course, bio, sections

st.set_page_config(page_title="Portfolio", layout="centered")
st.title(full_name)
st.subheader(course)

st.write(bio)

for title, content in sections.items():
    with st.expander(title):
        st.write(content)
