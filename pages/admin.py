import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Admin Dashboard 🔒",
    page_icon="🔒",
    layout="wide"
)

# Hide Streamlit branding
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title("🔒 Admin Dashboard")

DATA_FILE = "messages.csv"

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# Login screen
if not st.session_state.authenticated:
    password = st.text_input("Enter password:", type="password", key="pwd")
    
    if st.button("Login"):
        if password == "YourSecurePassword123":  # Change this to your secure password!
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("❌ Wrong password")
    st.stop()

# Admin panel (only shows after successful login)
st.success("✅ Logged in successfully!")

# Check if file exists
if not os.path.exists(DATA_FILE):
    st.warning("⚠️ No messages file found yet!")
    st.info("The file will be created when someone sends the first message.")
else:
    try:
        df = pd.read_csv(DATA_FILE)
        
        if len(df) > 0:
            st.info(f"📊 **Total Messages:** {len(df)}")
            
            # Sort by timestamp (newest first)
            df_sorted = df.sort_values('timestamp', ascending=False)
            
            st.subheader("📬 All Messages")
            
            # Display messages in expandable cards
            for idx, row in df_sorted.iterrows():
                with st.expander(f"📩 Message from {row['timestamp']}", expanded=True):
                    st.write(row['message'])
            
            st.divider()
            
            # Show data table
            st.subheader("📋 Full Data Table")
            st.dataframe(df_sorted, use_container_width=True)
            
            # Download button
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download All Messages (CSV)",
                data=csv,
                file_name="messages_export.csv",
                mime="text/csv"
            )
        else:
            st.warning("📭 No messages received yet!")
            st.info("Messages will appear here once someone sends one through your main app.")
            
    except Exception as e:
        st.error(f"❌ Error reading messages: {str(e)}")

# Logout button
st.divider()
if st.button("🚪 Logout"):
    st.session_state.authenticated = False
    st.rerun()
