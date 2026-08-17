🏦 Loan Approval Predictor

An end-to-end Machine Learning application that predicts whether a loan application is likely to be approved based on applicant financial and personal details.

The project uses Scikit-learn for machine learning, FastAPI for model serving, and Streamlit for the interactive web interface.

🌐 Live Demo

🚀 "Try the Loan Approval Predictor" (https://loan-approval-predictor-lovish-aggarwal.streamlit.app/)

✨ Features

- 🤖 Machine Learning-based loan approval prediction
- 📊 Data preprocessing and feature handling
- 🧠 Scikit-learn trained model
- ⚡ FastAPI-based API for model inference
- 🖥️ Interactive Streamlit interface
- 🌐 Deployed web application

🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Uvicorn

🔄 Workflow

Applicant Details
       ↓
Data Preprocessing
       ↓
Trained ML Model
       ↓
Loan Approval Prediction
       ↓
FastAPI / Streamlit
       ↓
Deployed Application

📂 Project Structure

Loan_Approval_Predictor/
│
├── Loan_Approval.ipynb
├── Model.pkl
├── app.py
├── streamlit_app.py
├── loan_approval_dataset.csv
├── requirements.txt
└── README.md

📄 File Description

File| Description
"Loan_Approval.ipynb"| Data analysis, preprocessing, model training and evaluation
"Model.pkl"| Trained Machine Learning model
"app.py"| FastAPI application for serving predictions
"streamlit_app.py"| Streamlit web application
"loan_approval_dataset.csv"| Dataset used for training
"requirements.txt"| Required Python dependencies
"README.md"| Project documentation

🧠 Machine Learning

The model is built using Scikit-learn and trained on loan application data.

The application takes relevant applicant and financial information as input and uses the trained model to predict whether the loan is likely to be approved.

⚡ FastAPI

FastAPI is used to expose the trained ML model through an API, allowing applications to send input data and receive predictions programmatically.

🖥️ Streamlit

Streamlit provides the user-friendly interface where users can enter loan application details and receive a prediction from the trained model.

🎯 Project Objective

The main objective of this project is to demonstrate an end-to-end Machine Learning deployment workflow, from data preprocessing and model training to API development and an interactive web application.

Data → Preprocessing → ML Model → API → Web Application → Deployment

🚀 Future Improvements

- Improve model performance through hyperparameter tuning
- Compare multiple ML algorithms
- Add model performance visualizations
- Improve input validation
- Add more advanced deployment and monitoring features

👨‍💻 Author

Lovish Aggarwal

B.Tech CSE (AI/ML) — UIET Kurukshetra

Interested in AI/ML, Generative AI, Deep Learning, Software Development, and building real-world AI applications.

---

⭐ If you found this project useful, consider giving the repository a star!
