
from src.utils.docs_utils.base_model import ResponseEmptyDictModel, MonthlyResponseModel, MonthlyIndividualResponseModel, DailyResponseModel, DailyIndividualResponseModel, YearlyResponseModel, YearlyIndividualResponseModel


def get_yearly_response(individual: bool, data):
    if individual:
        return {"application/json": {"example": YearlyResponseModel(
            ok=True,
            data=[data],
            message="Data periodically per month found!"
        )}}

    return {"application/json": {"example":YearlyIndividualResponseModel(
        ok=True,
        data=data,
        message="Data for specific month found!"
    )}}
def get_monthly_response(individual: bool, data):
    if individual:
        return {"application/json": {"example": MonthlyResponseModel(
            ok=True,
            data=[data],
            message="Data periodically per month found!"
        )}}

    return {"application/json": {"example":MonthlyIndividualResponseModel(
        ok=True,
        data=data,
        message="Data for specific month found!"
    )}}

def get_daily_response(individual: bool, data):
    if individual:
        return {"application/json": {"example": DailyResponseModel(
            ok=True,
            data=[data],
            message="Data periodically per day found!"
        )}}

    return {"application/json": {"example":DailyIndividualResponseModel(
        ok=True,
        data=data,
        message="Data for specific day found!"
    )}}


def get_empty_dict_response(message):
    return {"application/json": {"example": ResponseEmptyDictModel(
        ok=True,
        data={},
        message=message
    )}}
