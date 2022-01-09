import json
import re

from src.repository.daily_data_repository import DailyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse
from src.utils.reformat_date import concatenate_date
from src.utils.pattern_checker import check_params_pattern

from src.utils.check_data import check_if_data_result_is_null
router = APIRouter()

@router.get("")
def get_daily_data(response: Response, since : str = '2020.1.1', upto : str = 'nodata'):
    repository = DailyDataRepository(covid_driver=CovidDataDriver())

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)


    return check_if_data_result_is_null('day', response, repository, since, upto)

@router.get("/{year}")
def get_daily_given_year_data(year: int,response: Response, since: str = '1.1', upto : str = '12.31'):
    repository = DailyDataRepository(covid_driver=CovidDataDriver())

    since = concatenate_date(year, since)
    upto = concatenate_date(year, upto)

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    
    return check_if_data_result_is_null('day', response, repository, since, upto)

@router.get("/{year}/{month}")
def get_daily_given_year_data(year: int,month:int,response: Response, since: int = 1, upto : int = 31):
    repository = DailyDataRepository(covid_driver=CovidDataDriver())

    since = concatenate_date(year, month, since)
    upto = concatenate_date(year, month, upto)

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    
    return check_if_data_result_is_null('day', response, repository, since, upto)

@router.get("/{year}/{month}/{day}")
def get_daily_given_year_data(year: int,month:int, day:int, response: Response):
    repository = DailyDataRepository(covid_driver=CovidDataDriver())

    query = concatenate_date(year, month, day)

    params_pat = check_params_pattern('date',query)
   
    if (not params_pat):
        return CustomResponse().error_response(response, {}, "Params not matched with our rule!", 422)

    
    return check_if_data_result_is_null('day', response, repository, query, query, True)
    
    