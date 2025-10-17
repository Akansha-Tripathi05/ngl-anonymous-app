import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ------------------ SETTINGS ------------------
st.set_page_config(
    page_title="Anonymous Message Box 💌",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------ HIDE ALL STREAMLIT BRANDING (INCLUDING FORK BUTTON) ------------------
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display:none;}
        div[data-testid="stToolbar"] {display: none;}
        .stApp header {display: none;}
        [data-testid="stHeader"] {display: none;}
        button[kind="header"] {display: none;}
        div[data-testid="stDecoration"] {display: none;}
        .viewerBadge_link__qRIco {display: none;}
        .viewerBadge_container__r5tak {display: none;}
        header[data-testid="stHeader"] {display: none;}
        .stApp > header {display: none;}
        iframe {display: none;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ------------------ HIDDEN USER IDENTITY ------------------
USERNAME = "Akansha"  # <-- this will be saved in background
DATA_FILE = "messages.csv"

# Create the data file if it doesn't exist
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["timestamp", "username", "message"]).to_csv(DATA_FILE, index=False)

# ------------------ STYLING ------------------
st.markdown(
    """
    <style>
        body {
            background-color: #fef6fb;
        }
        .main {
            background-color: #fff;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        .stTextArea textarea {
            border-radius: 10px;
            border: 1px solid #d63384;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #d63384;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            padding: 8px 16px;
        }
        .stButton>button:hover {
            background-color: #c2185b;
        }
        h1, h2, h3, p {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ FRONTEND ------------------
st.markdown("<h1>💌 Send me an Anonymous Message</h1>", unsafe_allow_html=True)
st.write("Be honest, be kind, and say what's on your mind anonymously ❤️")

st.divider()

with st.form("message_form", clear_on_submit=True):
    message = st.text_area("Type your message here...", placeholder="Write something nice (or real 😅)...")
    submitted = st.form_submit_button("Send 💬")

    if submitted:
        if message.strip() == "":
            st.warning("Please write something before sending!")
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_entry = pd.DataFrame([[timestamp, USERNAME, message]], columns=["timestamp", "username", "message"])
            new_entry.to_csv(DATA_FILE, mode="a", header=False, index=False)
            st.success("✅ Message sent successfully! Thanks for sharing 💫")

st.divider()

# ------------------ SECURE ADMIN SECTION (HIDDEN BY DEFAULT) ------------------
# Initialize session state for admin authentication
if 'admin_authenticated' not in st.session_state:
    st.session_state.admin_authenticated = False

# Only show admin panel after password is entered correctly
if not st.session_state.admin_authenticated:
    # Hidden admin login (use a secret URL parameter or just keep this hidden)
    admin_password_input = st.text_input("🔒 Admin Access", type="password", key="admin_login", 
                                         help="For admin use only", placeholder="Enter password")
    
    if admin_password_input:
        if admin_password_input == "Akansha@2025":  # CHANGE THIS PASSWORD!
            st.session_state.admin_authenticated = True
            st.rerun()
        else:
            st.error("❌ Incorrect password")
else:
    # Admin is authenticated - show messages
    st.success("✅ Admin authenticated")
    
    if st.button("🚪 Logout"):
        st.session_state.admin_authenticated = False
        st.rerun()
    
    st.subheader("📬 Received Messages")
    
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        if len(df) > 0:
            # Display messages in reverse order (newest first)
            for idx, row in df.iloc[::-1].iterrows():
                with st.container():
                    st.markdown(f"**📅 {row['timestamp']}**")
                    st.info(row['message'])
                    st.divider()
        else:
            st.info("No messages yet 💌")
    else:
        st.info("No messages yet 💌")