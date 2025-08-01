import streamlit as st

st.set_page_config(page_title="Insightful | BI Automation", layout="centered")

st.markdown("# Say Goodbye to Excel Chaos. 🧹📊")
st.markdown("### Automate Your Reports with Python-Powered Dashboards.")

st.markdown("""
Insightful turns your spreadsheets into automated, client-ready dashboards and reports — fast. No BI team required.
""")

st.markdown("## ✅ What We Do")
st.markdown("""
**Insightful helps lean teams:**
- Eliminate copy/paste reporting workflows  
- Create dashboards that actually get used  
- Automate data pipelines without Power BI or Tableau overhead  
- Integrate Salesforce, Jotform, Mailchimp, and more  
""")

st.markdown("## 🧰 How It Works")
st.markdown("""
1. **You send us your existing reports** (Excel, CSV, Salesforce, etc.)  
2. **We build automated dashboards** using Python + Streamlit  
3. **You receive real-time or scheduled reports**, shared via web, email, or Slack  
""")

st.markdown("## 💵 Plans & Pricing")

st.markdown("### Starter — $399 setup + $49/month")
st.markdown("""
For automating a single painful report  
✅ 1 automated report  
✅ Basic dashboard (3 KPIs)  
✅ Scheduled output (email or web)  
""")

st.markdown("### Pro — $1,250 setup + $149/month")
st.markdown("""
Our most popular package  
✅ Up to 3 reports  
✅ Dashboard with filters and KPIs  
✅ Salesforce or Mailchimp integration  
✅ Monthly support and tuning  
""")

st.markdown("### Enterprise — from $3,000 + $349/month")
st.markdown("""
For sales or ops teams ready to scale BI  
✅ Unlimited dashboards  
✅ Full API integrations  
✅ Branded login-gated app  
✅ Priority support  
""")

st.markdown("## 🧩 Add-Ons")
st.markdown("""
- Historical data migration: +$350  
- Custom API connectors: +$250  
- AI forecasting module (beta): +$500  
- Dashboard UI redesign: +$750  
""")

st.markdown("## 🚀 Ready to See It in Action?")
st.markdown("""
Let’s talk about your first automation.

👉 **Email us at [info@heyinsightful.com](mailto:info@heyinsightful.com)**  
Or fill out our short form below and we’ll follow up within 24 hours.
""")

# Optional: Embed a Jotform or Google Form
st.markdown("### Contact Form")
st.components.v1.iframe("https://form.jotform.com/your_form_id_here", height=600)

