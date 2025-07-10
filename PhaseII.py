import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stats Explorer", layout="centered")
st.title("Calvin Johnson: Career Stats Explorer")

# Load data
data = pd.read_json("data.json")

# Initialize session state
if "year_range" not in st.session_state:
    st.session_state.year_range = (2007, 2015)

# Sidebar filters
start, end = st.slider("Select Year Range", 2007, 2015, st.session_state.year_range)
st.session_state.year_range = (start, end)
stat = st.selectbox("Choose statistic to view", ["receiving_yards", "touchdowns", "receptions"])

# Filtered data
df = data[(data.year >= start) & (data.year <= end)]

# Dynamic charts
st.subheader(f"{stat.replace('_', ' ').title()} by Season")
chart_data = df.set_index("year")[stat]
if stat == "touchdowns":
    st.line_chart(chart_data)
else:
    st.bar_chart(chart_data)

# Static pie chart
st.subheader("Receptions vs Touchdowns (All Seasons)")
counts = {
    "Receptions": int(data.receptions.sum()),
    "Touchdowns": int(data.touchdowns.sum())
}
fig, ax = plt.subplots()
ax.pie(counts.values(), labels=counts.keys(), autopct="%1.1f%%")
ax.axis("equal")
st.pyplot(fig)
