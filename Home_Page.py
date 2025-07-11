import streamlit as st

st.set_page_config(page_title="Home", layout="centered")
st.title("Calvin Johnson: A Georgia Tech Legend")
st.write("**Portfolio**: Detailed career overview and achievements of Calvin Johnson.")
st.write("**Stats Explorer**: Interactive dashboard of Calvin Johnson's career statistics.")


st.set_page_config(layout="centered")
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Portfolio", "Stats Explorer"])

if page == "Home":
    st.title("Calvin Johnson: A GT Legend")
    st.write("…your home page content…")
elif page == "Portfolio":
    import Portfolio  # runs Portfolio.py
elif page == "Stats Explorer":
    import PhaseII   # runs PhaseII.py
