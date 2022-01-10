import json

from src.repository.yearly_data_repository import YearlyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request, status
from src.utils.custom_response import CustomResponse

from src.utils.check_data import check_if_data_result_is_null
from src.utils.docs_utils.base_model import ResponseEmptyDictModel, YearlyResponseModel, YearlyIndividualResponseModel
from src.utils.docs_utils.get_response_docs import get_empty_dict_response, get_yearly_response
router = APIRouter()

example_data = {"year": "2021", "positive": 231299,
                "recovered": 131232, "deaths": 1233, "active": 81114}

@router.get("",responses={
    status.HTTP_200_OK: {
            "model": YearlyResponseModel,
            "content": get_yearly_response(False, example_data)
            },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "model": ResponseEmptyDictModel,
        "content": get_empty_dict_response("Query params not matched with our rule")
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ResponseEmptyDictModel,
        "content": get_empty_dict_response("No data found!")
    },
})
def get_yearly_data(response: Response,  since: int = 2020, upto: int = 9999999):
    repository = YearlyDataRepository(covid_driver=CovidDataDriver())

    return check_if_data_result_is_null('year', response, repository, since, upto)


@router.get("/{year}", responses={
    status.HTTP_200_OK: {
            "model": YearlyIndividualResponseModel,
            "content": get_yearly_response(True, example_data)
            },
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "model": ResponseEmptyDictModel,
        "content": get_empty_dict_response("Query params not matched with our rule")
    },
    status.HTTP_404_NOT_FOUND: {
        "model": ResponseEmptyDictModel,
        "content": get_empty_dict_response("No data found!")
    },
})
def get_yearly_data(year: int, response: Response):
    repository = YearlyDataRepository(covid_driver=CovidDataDriver())
    
    return check_if_data_result_is_null('year', response, repository, year, year, True)