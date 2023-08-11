from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class TimeSeries(BaseModel):
    from_symbol : str
    to_symbol : str
    date : datetime
    open : float
    high : float 
    low  : float 
    close: float 

class UserCount(BaseModel):
    total: int