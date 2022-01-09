import json

from src.repository.yearly_data_repository import YearlyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse

from src.utils.check_data import check_if_data_result_is_null
router = APIRouter()

@router.get("")
def get_yearly_data(response: Response,  since: int = 2020, upto: int = 9999999):
    repository = YearlyDataRepository(covid_driver=CovidDataDriver())

    return check_if_data_result_is_null('year', response, repository, since, upto)


@router.get("/{year}")
def get_yearly_data(year: int, response: Response):
    repository = YearlyDataRepository(covid_driver=CovidDataDriver())
    
    return check_if_data_result_is_null('year', response, repository, year, year, True)