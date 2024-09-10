from pydantic import BaseModel
from typing import Optional

class Features(BaseModel):
    foundersEquity: Optional[float] = None
    investorsEquity: Optional[float] = None
    employeesEquity: Optional[float] = None
    othersEquity: Optional[float] = None
    burnRate: Optional[float] = None
    runway: Optional[float] = None
    cac: Optional[float] = None
    activeUsers: Optional[float] = None
    revenue: Optional[float] = None
    netProfit: Optional[float] = None
    grossMargin: Optional[float] = None
    netMargin: Optional[float] = None
    retentionRate: Optional[float] = None
    mrrGrowth: Optional[float] = None
    ltvCacRatio: Optional[float] = None
    npsScore: Optional[float] = None
    conversionRate: Optional[float] = None

