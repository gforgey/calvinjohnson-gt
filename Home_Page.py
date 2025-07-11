# Home_Page.py

import streamlit as st  # ← Make sure this is the very first import

# Configure the page
st.set_page_config(
    page_title="Calvin Johnson: A GT Legend",
    page_icon="🐝",
    layout="wide"
)

# Header
st.markdown("<h1 style='color:#003057;'>Calvin Johnson: A Georgia Tech Legend 🐝</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color:#ce1126;'>CS 1301 – Intro to Computing</h3>", unsafe_allow_html=True)
st.markdown("---")

# Two‐column layout
col1, col2 = st.columns([1, 2])
with col1:
    # Use Streamlit’s built‐in image loader (no PIL needed)
    st.image("images/calvin.jpg", caption="Calvin “Megatron” Johnson", use_column_width=True)

with col2:
    st.write("""
    🔸 **Portfolio**  
      A detailed look at Calvin’s journey at Georgia Tech and beyond, with expandable sections.

    🔸 **Stats Explorer**  
      Interactive charts showing his yards, touchdowns, and receptions by season.
    """)

st.markdown("---")

# Quick radio nav
choice = st.radio("Quick Jump", ["Home", "Portfolio", "Stats Explorer"])
if choice == "Portfolio":
    st.write("🔗 Click **Portfolio** in the sidebar to view career expanders.")
elif choice == "Stats Explorer":
    st.write("🔗 Click **Stats Explorer** in the sidebar to explore stats.")
else:
    st.write("Welcome! Use the sidebar ☰ to navigate between pages.")
