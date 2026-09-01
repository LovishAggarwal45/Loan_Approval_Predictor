import streamlit as st
import requests
import time

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

API = "https://loan-approval-predictor-1voq.onrender.com/predict"

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Sora:wght@700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        #MainMenu, footer, header {visibility: hidden;}

        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 780px;
        }

        .app-header {
            text-align: center;
            padding: 2.4rem 1.4rem 2.2rem 1.4rem;
            background: linear-gradient(135deg, #0b1c2c 0%, #16324f 45%, #2c5364 100%);
            border-radius: 18px;
            margin-bottom: 1.8rem;
            box-shadow: 0 10px 26px rgba(11, 28, 44, 0.35);
            position: relative;
            overflow: hidden;
        }
        .app-header::before {
            content: "";
            position: absolute;
            top: -60px;
            right: -60px;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle, rgba(255,255,255,0.10) 0%, rgba(255,255,255,0) 70%);
        }
        .app-header .eyebrow {
            display: inline-block;
            color: #9fd6c7;
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }
        .app-header h1 {
            font-family: 'Sora', 'Inter', sans-serif;
            color: #ffffff;
            font-size: 2.3rem;
            font-weight: 800;
            margin: 0 0 0.45rem 0;
            letter-spacing: -0.03em;
            line-height: 1.15;
        }
        .app-header h1 span {
            background: linear-gradient(90deg, #7ee8c0 0%, #a0d8ef 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .app-header p {
            color: #c9d6de;
            font-size: 0.95rem;
            margin: 0;
            font-weight: 400;
        }

        .section-title {
            font-size: 1rem;
            font-weight: 700;
            color: #1a2530;
            margin: 1.4rem 0 0.6rem 0;
            padding-bottom: 0.4rem;
            border-bottom: 2px solid #eef1f4;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 14px !important;
            border: 1px solid #e7ebee !important;
            padding: 0.4rem 0.2rem !important;
            background: #ffffff;
        }

        .badge {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.65rem 0.9rem;
            border-radius: 10px;
            font-size: 0.87rem;
            font-weight: 500;
            margin-bottom: 0.55rem;
        }
        .badge-green   { background: #eafaf1; color: #1b7a43; border: 1px solid #bdeed2; }
        .badge-blue    { background: #eaf3fb; color: #1a5fa0; border: 1px solid #bfdcf3; }
        .badge-yellow  { background: #fdf6e6; color: #92650a; border: 1px solid #f6e3ad; }
        .badge-red     { background: #fdecec; color: #a3231f; border: 1px solid #f6c5c3; }
        .badge-gray    { background: #f3f4f6; color: #4b5563; border: 1px solid #e2e5e9; }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 700;
            font-size: 0.95rem;
            padding: 0.65rem 0;
            background: linear-gradient(135deg, #16324f 0%, #2c5364 100%);
            border: none;
            transition: all 0.15s ease-in-out;
        }
        div.stButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 14px rgba(22, 50, 79, 0.3);
        }

        .result-card {
            padding: 1.4rem;
            border-radius: 14px;
            text-align: center;
            margin-top: 1rem;
        }
        .result-approved {
            background: linear-gradient(135deg, #e5f9ee 0%, #d3f3e2 100%);
            border: 1px solid #a9e6c4;
        }
        .result-rejected {
            background: linear-gradient(135deg, #fdeceb 0%, #fbdedb 100%);
            border: 1px solid #f0b7b3;
        }
        .result-card h2 { margin: 0 0 0.3rem 0; font-size: 1.4rem; }
        .result-card p  { margin: 0; color: #4b5563; font-size: 0.9rem; }

        .app-footer {
            text-align: center;
            color: #9aa4ad;
            font-size: 0.78rem;
            margin-top: 2.2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-header">
        <span class="eyebrow">Machine Learning · Credit Risk</span>
        <h1>🏦 Loan <span>Approval</span> Predictor</h1>
        <p>Instant, model-driven risk assessment for personal loan applications</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">👤 Applicant Details</div>', unsafe_allow_html=True)

with st.container(border=True):
    c1, c2 = st.columns(2)
    with c1:
        dependents = st.number_input("Dependents", 0, 5, 1)
        education = st.selectbox("Education", [" Graduate", " Not Graduate"])
        income = st.number_input("Annual Income (₹)", 100000, 10000000, 500000, 50000)
    with c2:
        self_employed = st.selectbox("Self Employed", [" No", " Yes"])
        loan = st.number_input("Loan Amount (₹)", 100000, 10000000, 1000000, 100000)
        term = st.number_input("Loan Term (Years)", 1, 50, 10)

st.markdown('<div class="section-title">📊 Credit & Assets</div>', unsafe_allow_html=True)

with st.container(border=True):
    cibil = st.slider("CIBIL Score", 300, 900, 750)

    c1, c2 = st.columns(2)
    with c1:
        residential = st.number_input("Residential Assets (₹)", 0, 10000000, 1000000, 100000)
        commercial = st.number_input("Commercial Assets (₹)", 0, 10000000, 500000, 100000)
    with c2:
        luxury = st.number_input("Luxury Assets (₹)", 0, 10000000, 200000, 100000)
        bank = st.number_input("Bank Assets (₹)", 0, 10000000, 500000, 100000)

ratio = loan / income

st.markdown('<div class="section-title">💡 Quick Insights</div>', unsafe_allow_html=True)

if cibil >= 750:
    st.markdown('<div class="badge badge-green">🟢 &nbsp;Excellent CIBIL score</div>', unsafe_allow_html=True)
elif cibil >= 700:
    st.markdown('<div class="badge badge-blue">🔵 &nbsp;Good CIBIL score</div>', unsafe_allow_html=True)
elif cibil >= 650:
    st.markdown('<div class="badge badge-yellow">🟡 &nbsp;Fair CIBIL score</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="badge badge-red">🔴 &nbsp;Low CIBIL score</div>', unsafe_allow_html=True)

if ratio > 5:
    st.markdown(
        '<div class="badge badge-yellow">⚠️ &nbsp;Loan amount is high relative to annual income</div>',
        unsafe_allow_html=True,
    )
elif ratio <= 3:
    st.markdown(
        '<div class="badge badge-gray">📐 &nbsp;Loan amount looks reasonable relative to income</div>',
        unsafe_allow_html=True,
    )

st.write("")

if st.button("🔮 Predict Loan Approval", type="primary", use_container_width=True):

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
        "bank_asset_value": bank,
    }

    with st.spinner("🔎 Analyzing application with the prediction model..."):
        try:
            start = time.time()
            r = requests.post(API, json=data)
            elapsed = time.time() - start
            if elapsed < 0.6:
                time.sleep(0.6 - elapsed)

            if r.status_code == 200:
                result = r.json()["Loan Approval Status"]

                if result == "Approved":
                    st.markdown(
                        """
                        <div class="result-card result-approved">
                            <h2>🎉 Loan Approved</h2>
                            <p>Your application matches the model's approval pattern.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    st.balloons()
                else:
                    st.markdown(
                        """
                        <div class="result-card result-rejected">
                            <h2>❌ Loan Rejected</h2>
                            <p>The model found this application less likely to be approved.
                            Possible factors include CIBIL score, income, loan amount or assets.</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.error("API Error. Please try again.")

        except requests.exceptions.ConnectionError:
            st.error("⚠️ The prediction server is not reachable. Please try again shortly.")

st.markdown(
    """
    <div class="app-footer">
        Loan Approval Prediction Model &nbsp;•&nbsp; Built by Lovish Aggarwal &nbsp;•&nbsp; B.Tech CSE (AI &amp; ML)
    </div>
    """,
    unsafe_allow_html=True,
)