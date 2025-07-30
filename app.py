import streamlit as st

st.set_page_config(page_title="HeyInsightful", layout="centered")

st.title("👋 HeyInsightful")
st.subheader("Your Python-powered BI sidekick")

st.markdown("""
Escape spreadsheet chaos. Automate your dashboards and get real insights — 
no bloat, no coding required.
""")

with st.form("email_form"):
    email = st.text_input("Join the waitlist")
    submitted = st.form_submit_button("Notify Me")
    if submitted and email:
        st.success(f"Thanks! We'll reach out to {email} soon.")
