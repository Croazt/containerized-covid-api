import json
import re

from src.repository.periodically_data_repository import PeriodicallyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse
from src.utils.reformat_date import concatenate_date
from src.utils.pattern_checker import check_params_pattern
router = APIRouter()

@router.get("")
def get_daily_data(response: Response, request: Request, since : str = '2020.1.1', upto : str = 'nodata'):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    data = repository.get_daily_data(since=since, upto=upto)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data per month found!",)

@router.get("/{year}")
def get_daily_given_year_data(year: int,response: Response, request: Request, since: str = '1.1', upto : str = '12.31'):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())

    since = concatenate_date(year, since)
    upto = concatenate_date(year, upto)

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    data = repository.get_daily_data(since=since, upto=upto)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data for specific year found!",)

@router.get("/{year}/{month}")
def get_daily_given_year_data(year: int,month:int,response: Response, request: Request, since: int = 1, upto : int = 31):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())

    since = concatenate_date(year, month, since)
    upto = concatenate_date(year, month, upto)

    since_pat = check_params_pattern('date',since)
    upto_pat = check_params_pattern('date',upto)
   
    if (not since_pat) or (upto != 'nodata' and not (upto_pat)):
        return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)

    data = repository.get_daily_data(since=since, upto=upto)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data for specific year found!",)

    
    