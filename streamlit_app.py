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

# ------------------ HIDE ALL STREAMLIT BRANDING INCLUDING BOTTOM PROFILE ------------------
hide_streamlit_style = """
    <style>
        /* Hide main menu, footer, header */
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        header {visibility: hidden !important;}
        
        /* Hide all header elements */
        .stApp > header {display: none !important;}
        [data-testid="stHeader"] {display: none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        div[data-testid="stDecoration"] {display: none !important;}
        div[data-testid="stStatusWidget"] {display: none !important;}
        
        /* Hide Fork button and GitHub icon */
        button[kind="header"] {display: none !important;}
        button[kind="headerNoPadding"] {display: none !important;}
        .viewerBadge_link__qRIco {display: none !important;}
        .viewerBadge_container__r5tak {display: none !important;}
        .styles_viewerBadge__CvC9N {display: none !important;}
        
        /* Hide profile picture and action elements */
        [data-testid="stHeaderActionElements"] {display: none !important;}
        .stApp header [data-testid="stImage"] {display: none !important;}
        
        /* Hide deploy button */
        .stDeployButton {display: none !important;}
        
        /* Hide bottom profile section and "Created by" link */
        .css-1dp5vir {display: none !important;}
        .css-164nlkn {display: none !important;}
        [data-testid="stSidebarUserContent"] {display: none !important;}
        .stApp [data-testid="stBottomBlockContainer"] {display: none !important;}
        div[data-testid="stBottom"] {display: none !important;}
        
        /* Hide any footer content including profile */
        .reportview-container .main footer {display: none !important;}
        footer {display: none !important;}
        .footer {display: none !important;}
        
        /* Hide creator badge/profile at bottom */
        a[href*="streamlit.io"] {display: none !important;}
        a[href*="github.com"] {display: none !important;}
        
        /* Nuclear option for bottom elements */
        .stApp > footer {display: none !important;}
        [class*="viewerBadge"] {display: none !important;}
        
        /* Remove top padding */
        .block-container {padding-top: 1rem !important;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem !important;}
        
        /* Nuclear option - hide entire header container */
        header[data-testid="stHeader"] {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
            position: absolute !important;
            top: -9999px !important;
        }
        
        /* Hide any iframes */
        iframe {display: none !important;}
        
        /* Hide streamlit branding watermark */
        ._container_gzau3_1 {display: none !important;}
        
        /* Additional selectors for profile badge */
        div[class*="UserBadge"] {display: none !important;}
        div[class*="profileBadge"] {display: none !important;}
        button[class*="UserBadge"] {display: none !important;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ------------------ HIDDEN USER IDENTITY ------------------
USERNAME = "Akansha"
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