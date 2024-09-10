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
    foundersEquity = data['foundersEquity']
    investorsEquity = data['investorsEquity']
    employeesEquity = data['employeesEquity']
    othersEquity = data['othersEquity']
    burnRate = data['burnRate']
    runway = data['runway']
    cac = data['cac']
    activeUsers = data['activeUsers']
    revenue = data['revenue']
    netProfit = data['netProfit']
    grossMargin = data['grossMargin']
    netMargin = data['netMargin']
    retentionRate = data['retentionRate']
    mrrGrowth = data['mrrGrowth']
    ltvCacRatio = data['ltvCacRatio']
    npsScore = data['npsScore']
    conversionRate = data['conversionRate']

    # Make the prediction
    prediction = model.predict_proba([[foundersEquity, investorsEquity, employeesEquity, othersEquity,
                                 burnRate, runway, cac, activeUsers, revenue, netProfit, grossMargin,
                                 netMargin, retentionRate, mrrGrowth, ltvCacRatio, npsScore, conversionRate]])[:, 1]
    print("success probablity of your startup based on the data is",prediction)



# Run only if not in an interactive environment
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

