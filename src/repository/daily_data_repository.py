import datetime as dt

from src.interface.driver.covid_data import CovidDataDriverInt
from src.interface.repository.periodically_data_repository import PeriodicallyDataRepository
from src.domain.periodically_data import Yearly, Monthly, Daily

from src.utils.reformat_date import replace_fillz, concatenate_date
from src.utils.dataframe_transform import transform_df
class DailyDataRepository(PeriodicallyDataRepository):
    covid_driver: CovidDataDriverInt

    def __init__(self, covid_driver: CovidDataDriverInt):
        self.covid_driver = covid_driver
        self.date_now = dt.datetime.now()

   
    def get_data(self, since = "2020.1.1" , upto = "nodata") :
        data = self.covid_driver.get_data_periodic()
        
        if upto == 'nodata' :
            upto = concatenate_date(self.date_now.year, self.date_now.month, self.date_now.day)
        
        upto, since = replace_fillz(upto), replace_fillz(since)
        
        if  upto < since :
            return Daily(values=[])

        res = transform_df(is_type='date', df=data, since=since, upto=upto)

        return Daily(res.to_dict(orient="records"))

def reformat_upto_since(upto,since):
    return replace_fillz(upto), replace_fillz(since)