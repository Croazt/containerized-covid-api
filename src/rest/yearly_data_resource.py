from src.repository.periodically_data_repository import PeriodicallyDataRepository
from src.driver.covid_data import CovidDataDriver
from fastapi import  FastAPI, APIRouter, Response, Request
from src.utils.custom_response import CustomResponse

router = APIRouter()

@router.get("")
def get_yearly_data(response : Response, request : Request) :
    repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
    since = None
    upto = None
    if 'since' in request.query_params :
        since = request.query_params['since']

    if 'upto' in request.query_params :
        upto = request.query_params['upto']

    data = []
    if since != None and upto != None :
        data = repository.get_yearly_data(since=since,upto=upto)
    elif since != None :
        data = repository.get_yearly_data(since=since)
    elif upto != None :
        data = repository.get_yearly_data(upto=upto)
    else :
        data = repository.get_yearly_data()

    if len(data.values) < 1 :
        return CustomResponse().error_response(response, {}, "No data found!", 204)

    return CustomResponse().success_response(response, data.values, "Data per year found!",)