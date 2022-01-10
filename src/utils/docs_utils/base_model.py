from pydantic import  BaseModel
from src.domain.periodically_data import Daily, Day, Yearly, Year, Monthly, Month, General

from typing import List

class GeneralResponseModel(BaseModel):
    ok: bool = True
    message: str
    data: General

class YearlyResponseModel(BaseModel):
    ok: bool = True
    data: List[Year]
    message: str
    
class MonthlyResponseModel(BaseModel):
    ok: bool = True
    data: List[Month]
    message: str
    
class DailyResponseModel(BaseModel):
    ok: bool = True
    data: List[Day]
    message: str

class YearlyIndividualResponseModel(BaseModel):
    ok: bool = True
    data: Year
    message: str
    
class MonthlyIndividualResponseModel(BaseModel):
    ok: bool = True
    data: Month
    message: str

class DailyIndividualResponseModel(BaseModel):
    ok: bool = True
    message: str
    data: Day

class ResponseEmptyDictModel(BaseModel):
    ok: bool = False
    message: str
    data: dict