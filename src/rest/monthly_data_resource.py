import json
import re

from src.repository.monthly_data_repository import MonthlyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse
from src.utils.reformat_date import concatenate_date

from src.utils.check_data import check_if_data_result_is_null
router = APIRouter()

@router.get("")
def get_monthly_data(response: Response, request: Request, since : str = '2020.1', upto : str = 'nodata'):
    repository = MonthlyDataRepository(covid_driver=CovidDataDriver())

    pattern1 = re.compile("^[0-9][0-9][0-9][0-9].[0-9][0-9]")
    pattern2 = re.compile("^[0-9][0-9][0-9][0-9].[0-9]")
   
    if (not (pattern1.match(since) or pattern2.match(since))) or (upto != 'nodata' and not (pattern1.match(upto) or pattern2.match(upto))):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    return check_if_data_result_is_null('month', response, repository, since, upto)

@router.get("/{year}")
def get_monthly_given_year_data(year: int,response: Response, request: Request, since: int = 1, upto : int = 12):
    repository = MonthlyDataRepository(covid_driver=CovidDataDriver())

    since = concatenate_date(year, since)
    upto = concatenate_date(year, upto)

    return check_if_data_result_is_null('month', response, repository, since, upto)

    
@router.get("/{year}/{month}")
def get_month_recap_data(year: int, month : int, response: Response, request: Request):
    repository = MonthlyDataRepository(covid_driver=CovidDataDriver())

    query = concatenate_date(year, month)
    
    return check_if_data_result_is_null('month', response, repository, query, query, True)
