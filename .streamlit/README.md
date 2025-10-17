# NGL-style Streamlit app

A simple Streamlit app to receive anonymous messages and store them to messages.csv.

Run locally:
1. python -m venv .venv
2. source .venv/bin/activate   # or .venv\Scripts\activate on Windows
3. pip install -r requirements.txt
4. streamlit run streamlit_app.py

Deploy: push to GitHub and connect the repository to Streamlit Community Cloud.
Set the secret `admin_password` in Streamlit Cloud app settings for admin access.
