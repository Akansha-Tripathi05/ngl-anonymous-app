import streamlit as st
import pandas as pd
from datetime import datetime
import os

# ------------------ SETTINGS ------------------
st.set_page_config(page_title="Anonymous Message Box 💌", page_icon="💌", layout="centered")

# Hidden user identity (you can set your name or handle)
USERNAME = "Akansha"  # <-- change this to your name or unique handle
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
st.write("Be honest, be kind, and say what’s on your mind anonymously ❤️")

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

# ------------------ ADMIN SECTION ------------------
with st.expander("🔒 Admin Panel"):
    password = st.text_input("Enter admin password:", type="password")
    if password == "admin123":  # change this password
        df = pd.read_csv(DATA_FILE)
        st.dataframe(df)
    elif password:
        st.error("Incorrect password ❌")
