import json
import re

from src.repository.periodically_data_repository import PeriodicallyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse

router = APIRouter()

@router.get("")
def get_monthly_data(response: Response, request: Request):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())

    pattern1 = re.compile("^[0-9][0-9][0-9][0-9].[0-9][0-9]")
    pattern2 = re.compile("^[0-9][0-9][0-9][0-9].[0-9]")

    since = '2020.1'
    upto = 'nodata'
    
    if 'since' in request.query_params :
        temp = request.query_params['since']
        if not (pattern1.match(temp) or pattern2.match(temp)):
            return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)
        since = request.query_params['since']

    if 'upto' in request.query_params :
        temp = request.query_params['upto']
        if not (pattern1.match(temp) or pattern2.match(temp)):
            return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)
        upto = request.query_params['upto']

    data = repository.get_monthly_data(since=since, upto=upto)
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data per month found!",)

@router.get("/{year}")
def get_yearly_data(year: int, response: Response, request: Request):
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())

    since, upto = 1, 12
    
    if 'since' in request.query_params :
        temp = request.query_params['since']
        if not temp.isnumeric() :
            return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)
        
        if not int(temp) < since :
            since = request.query_params['since']
    
    if 'upto' in request.query_params :
        temp = request.query_params['upto']
        if not temp.isnumeric() :
            return CustomResponse().error_response(response, {}, "Query params not matched with our rule!", 422)
        
        if not int(temp) > upto :
            upto = request.query_params['upto']

    since = str(year) + '.' + str(since)
    upto = str(year) + '.' + str(upto)

    if upto < since :
        since, upto = upto, since

    data = repository.get_monthly_data(since=since, upto=upto)
 
    if len(data.values) < 1:
        return json.dumps(CustomResponse().error_response(response, {}, "No data found!", 204))

    return CustomResponse().success_response(response, data.values, "Data for specific year found!",)