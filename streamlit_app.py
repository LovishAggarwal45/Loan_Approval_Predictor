import streamlit as st
import requests

st.set_page_config(page_title="Loan Predictor", page_icon="🏦")

st.title("🏦 Loan Approval Predictor")
st.caption("Predict loan approval using Machine Learning")
st.caption("Created by Lovish Aggarwal ❤️")
st.divider()

API="http://127.0.0.1:8000/predict"

# Applicant Details
st.subheader("👤 Applicant Details")

c1, c2 = st.columns(2)

with c1:
    dependents = st.number_input("Dependents", 0, 5, 1)
    education = st.selectbox("Education", [" Graduate", " Not Graduate"])
    income = st.number_input(
        "Annual Income (₹)", 100000, 10000000, 500000, 50000
    )

with c2:
    self_employed = st.selectbox("Self Employed", [" No", " Yes"])
    loan = st.number_input(
        "Loan Amount (₹)", 100000, 10000000, 1000000, 100000
    )
    term = st.number_input("Loan Term (Years)", 1, 50, 10)

# Credit & Assets
st.subheader("📊 Credit & Assets")

c1, c2 = st.columns(2)

with c1:
    cibil = st.slider("CIBIL Score", 300, 900, 750)
    residential = st.number_input("Residential Assets (₹)", 0, 10000000, 1000000, 100000)
    commercial = st.number_input("Commercial Assets (₹)", 0, 10000000, 500000, 100000)

with c2:
    luxury = st.number_input("Luxury Assets (₹)", 0, 10000000, 200000, 100000)
    bank = st.number_input("Bank Assets (₹)", 0, 10000000, 500000, 100000)

# Small useful insight
ratio = loan / income

if cibil >= 750:
    st.success("🟢 Excellent CIBIL Score")
elif cibil >= 700:
    st.info("🔵 Good CIBIL Score")
elif cibil >= 650:
    st.warning("🟡 Fair CIBIL Score")
else:
    st.error("🔴 Low CIBIL Score")

if ratio > 5:
    st.warning("⚠️ Loan amount is high compared with annual income.")
elif ratio <= 3:
    st.info("💡 Loan amount looks reasonable compared with annual income.")

st.divider()

# Prediction
if st.button("🔮 Predict Loan Approval", type="primary",
             use_container_width=True):

    data = {
        "dependents": dependents,
        "education": education,
        "self_employed": self_employed,
        "income_annum": income,
        "loan_amount": loan,
        "loan_term": term,
        "cibil_score": cibil,
        "residential_assets_value": residential,
        "commercial_assets_value": commercial,
        "luxury_assets_value": luxury,
        "bank_asset_value": bank
    }

    try:
        r = requests.post(API, json=data)

        if r.status_code == 200:
            result = r.json()["Loan Approval Status"]

            if result == "Approved":
                st.success("🎉 Loan Approved!")
                st.write("Your application matches the model's approval pattern.")
                st.balloons()
            else:
                st.error("❌ Loan Rejected")
                st.write(
                    "The model found the application less likely to be approved. "
                    "Possible factors include CIBIL score, income, loan amount or assets."
                )
        else:
            st.error("API Error. Please try again.")

    except requests.exceptions.ConnectionError:
        st.error("⚠️ FastAPI server is not running.")

st.divider()
st.caption("🏦Loan Approval Prediction model | Created by Lovish Aggarwal ❤️ | B.Tech CSE(AI ML)")