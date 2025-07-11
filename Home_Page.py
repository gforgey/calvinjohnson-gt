
# Page config
st.set_page_config(
    page_title="Calvin Johnson: A GT Legend",
    page_icon="🐝",
    layout="wide"
)

# — Custom CSS for GT colors & styling —
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .header {
        color: #003057;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.2rem;
    }
    .subheader {
        color: #ce1126;
        font-size: 1.5rem;
        margin-top: 0;
    }
    .nav-radio > div {
        padding: 0.5rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# — Header —
st.markdown('<p class="header">Calvin Johnson: A Georgia Tech Legend 🐝</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">CS 1301 – Intro to Computing</p>', unsafe_allow_html=True)
st.markdown("---")

# — Two-column intro with image —
col1, col2 = st.columns([1, 2])
with col1:
    # make sure you have calvin.jpg in your images folder
    img = Image.open("images/calvin.jpg")
    st.image(img, use_column_width=True, caption="Calvin “Megatron” Johnson")
with col2:
    st.write(
        """
        🔸 **Portfolio**  
        A deep dive into Calvin’s journey—from record-breaking GT seasons to a Hall of Fame NFL career—using interactive expanders.

        🔸 **Stats Explorer**  
        Dynamic charts and filters let you explore his receiving yards, touchdowns, and more across every season.
        """
    )

st.markdown("---")

# — Optional Radio-nav (redundant with sidebar, but can help) —
choice = st.radio(
    "Quick Jump:",
    options=["Home", "Portfolio", "Stats Explorer"],
    key="home_nav",
    format_func=lambda x: x if x=="Home" else ("Portfolio" if x=="Portfolio" else "Stats Explorer")
)

if choice == "Portfolio":
    st.write("➡️ Select **Portfolio** from the sidebar to view your custom expanders.")
elif choice == "Stats Explorer":
    st.write("➡️ Select **Stats Explorer** from the sidebar to dive into interactive charts.")
else:
    st.write("Welcome! Use the sidebar (☰) or the radio buttons above to navigate through the app.")
