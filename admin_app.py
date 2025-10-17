import streamlit as st
import pandas as pd

st.title("🔒 Admin Dashboard")

password = st.text_input("Enter password:", type="password")

if password == "YourSecurePassword123":  # Change this!
    if st.button("Load Messages"):
        df = pd.read_csv("messages.csv")
        st.dataframe(df)
        
        # Download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Messages",
            data=csv,
            file_name="messages.csv",
            mime="text/csv"
        )
else:
    if password:
        st.error("Wrong password")