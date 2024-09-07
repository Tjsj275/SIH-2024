from pydantic import BaseModel

class Features(BaseModel):
    foundersEquity:float
    investorsEquity:float
    employeesEquity:float
    othersEquity:float
    burnRate:float
    runway:float
    cac:float
    activeUsers:float
    revenue:float
    netProfit:float
    grossMargin:float
    netMargin:float
    retentionRate:float
    mrrGrowth:float
    ltvCacRatio:float
    npsScore:float
    conversionRate:float

