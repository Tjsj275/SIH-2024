import uvicorn
from fastapi import FastAPI
from Features import Features
import numpy as np
import pickle
import pandas as pd
import nest_asyncio

nest_asyncio.apply()

app = FastAPI()

# Load the model
pickle_in = open("xgboost_model.pkl", "rb")
model = pickle.load(pickle_in)

# Define routes
@app.get('/')
def index():
    return {'Index route'}

@app.post('/prediction')
def predict_success(data: Features):
    data = data.dict()
    foundersEquity = data['foundersEquity'] if data['foundersEquity'] is not None else 0.0
    investorsEquity = data['investorsEquity'] if data['investorsEquity'] is not None else 0.0
    employeesEquity = data['employeesEquity'] if data['employeesEquity'] is not None else 0.0
    othersEquity = data['othersEquity'] if data['othersEquity'] is not None else 0.0
    burnRate = data['burnRate'] if data['burnRate'] is not None else 0.0
    runway = data['runway'] if data['runway'] is not None else 0.0
    cac = data['cac'] if data['cac'] is not None else 0.0
    activeUsers = data['activeUsers'] if data['activeUsers'] is not None else 0.0
    revenue = data['revenue'] if data['revenue'] is not None else 0.0
    netProfit = data['netProfit'] if data['netProfit'] is not None else 0.0
    grossMargin = data['grossMargin'] if data['grossMargin'] is not None else 0.0
    netMargin = data['netMargin'] if data['netMargin'] is not None else 1.0
    retentionRate = data['retentionRate'] if data['retentionRate'] is not None else 0.0
    mrrGrowth = data['mrrGrowth'] if data['mrrGrowth'] is not None else 0.0
    ltvCacRatio = data['ltvCacRatio'] if data['ltvCacRatio'] is not None else 0.0
    npsScore = data['npsScore'] if data['npsScore'] is not None else 0.0
    conversionRate = data['conversionRate'] if data['conversionRate'] is not None else 0.0

    # Make the prediction
    prediction = model.predict_proba([[foundersEquity, investorsEquity, employeesEquity, othersEquity,
                                 burnRate, runway, cac, activeUsers, revenue, netProfit, grossMargin,
                                 netMargin, retentionRate, mrrGrowth, ltvCacRatio, npsScore, conversionRate]])
    print("success probablity of your startup based on the data is",prediction[:,1])

# Run only if not in an interactive environment
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

