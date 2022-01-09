import datetime as dt

from src.interface.driver.covid_data import CovidDataDriverInt
from src.interface.repository.periodically_data_repository import PeriodicallyDataRepository
from src.domain.periodically_data import Yearly, Monthly, Daily

from src.utils.reformat_date import replace_fillz, concatenate_date
from src.utils.dataframe_transform import transform_df
class YearlyDataRepository(PeriodicallyDataRepository):
    covid_driver: CovidDataDriverInt

    def __init__(self, covid_driver: CovidDataDriverInt):
        self.covid_driver = covid_driver
        self.date_now = dt.datetime.now()

   
    def get_data(self, since : int = 2020, upto : int = 9999999) -> Yearly:
        data = self.covid_driver.get_data_periodic()
        
        if upto == 9999999 :
            upto = int(self.date_now.year)

        if  upto < since :
            return Yearly(values=[])
        
        res = transform_df(is_type='year', df=data, since=since, upto=upto)

        return Yearly(res.to_dict(orient="records"))
