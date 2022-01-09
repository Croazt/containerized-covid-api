import json

from src.repository.periodically_data_repository import PeriodicallyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse

router = APIRouter()

@router.get("")
def get_yearly_data(response: Response,  since: int = 2022, upto: int = 9999999):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
    data = repository.get_yearly_data(since=since, upto=upto)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data per year found!",)


@router.get("/{year}")
def get_yearly_data(year: int, response: Response):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
    
    data = repository.get_yearly_data(since=year, upto=year)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values[0], "Data for specific year found!",)