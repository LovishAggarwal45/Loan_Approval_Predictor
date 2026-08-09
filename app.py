from fastapi import FastAPI
from typing import Literal
import joblib 
import pandas as pd
from pydantic import BaseModel, Field

app=FastAPI()

model=joblib.load("Model.pkl")
columns=[' no_of_dependents', ' education', ' self_employed',
       ' income_annum', ' loan_amount', ' loan_term', ' cibil_score',
       ' residential_assets_value', ' commercial_assets_value',
       ' luxury_assets_value', ' bank_asset_value']

class Feature(BaseModel):
    dependents: int =Field(ge=0,le=5)
    education:Literal[" Graduate"," Not Graduate"]
    self_employed:Literal[" Yes"," No"]
    income_annum: float=Field(ge=0)
    loan_amount: float=Field(gt=0)
    loan_term: int=Field(gt=0,le=50)
    cibil_score:int=Field(ge=300,le=900)
    residential_assets_value: float=Field(ge=0)
    commercial_assets_value: float=Field(ge=0)
    luxury_assets_value: float=Field(ge=0)
    bank_asset_value: float=Field(ge=0)

@app.get("/")
def home():
    return {"message":"Loan Risk Prediction..."}

@app.post("/predict")
def predict(data:Feature):
    input_row = pd.DataFrame([{
        ' no_of_dependents'             :data.dependents,
        ' education'                    :data.education,
        ' self_employed'                :data.self_employed,
        ' income_annum'                 :data.income_annum,
        ' loan_amount'                  :data.loan_amount,
        ' loan_term'                    :data.loan_term,
        ' cibil_score'                  :data.cibil_score,
        ' residential_assets_value'     :data.residential_assets_value,
        ' commercial_assets_value'      :data.commercial_assets_value,
        ' luxury_assets_value'          :data.luxury_assets_value,
        ' bank_asset_value'             :data.bank_asset_value,
    }])
    
    prediction = model.predict(input_row)[0]
    return {"Loan Approval Status":("Approved" if prediction==1 else "Rejected")}