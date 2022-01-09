import datetime as dt

from src.interface.driver.covid_data import CovidDataDriverInt
from src.interface.repository.periodically_data_repository import PeriodicallyDataRepository
from src.domain.periodically_data import Yearly

class PeriodicallyDataRepository(PeriodicallyDataRepository):
    covid_driver: CovidDataDriverInt

    def __init__(self, covid_driver: CovidDataDriverInt):
        self.covid_driver = covid_driver
        self.date_now = dt.datetime.now()

    def get_yearly_data(self, since = "2020", upto = "2024") -> Yearly:
        data = self.covid_driver.get_data_periodic()

        res = data.groupby(['year'])['positive','recovered','deaths'].sum().reset_index()
        
        res['active'] = res['positive'] - res['recovered'] - res['deaths']
        res =Yearly(res.to_dict(orient="records"))

        return res