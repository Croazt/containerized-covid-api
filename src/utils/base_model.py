from pydantic import BaseModel, EmailStr
from src.domain.periodically_data import Yearly,Year,Daily, Day, General
from typing import List

class GeneralResponseModel(BaseModel) :
    ok : bool
    data : General
    message : str

class DailyResponseModel(BaseModel) :
    ok : bool
    data : List[Day]
    message : str
