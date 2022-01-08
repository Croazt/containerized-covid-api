from src.repository.general_data_repository import GeneralDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import  FastAPI, APIRouter, Response, status
from src.utils.custom_response import CustomResponse


def get_general_data(response : Response):
    repository = GeneralDataRepository(covid_driver=CovidDataDriver())
    data = repository.get_general_data()
    return CustomResponse().success_response(response, data, "Successfully getting data!")