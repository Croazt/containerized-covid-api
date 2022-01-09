import datetime as dt

from src.interface.driver.covid_data import CovidDataDriverInt
from src.interface.repository.periodically_data_repository import PeriodicallyDataRepository
from src.domain.periodically_data import Yearly, Monthly

class PeriodicallyDataRepository(PeriodicallyDataRepository):
    covid_driver: CovidDataDriverInt

    def __init__(self, covid_driver: CovidDataDriverInt):
        self.covid_driver = covid_driver
        self.date_now = dt.datetime.now()

    def get_yearly_data(self, since = "2020", upto = "nodata") -> Yearly:
        data = self.covid_driver.get_data_periodic()
        
        if upto == "nodata" :
            upto = str(self.date_now.year)

        if  upto < since :
            return Yearly(values=[])
        

        res = data.groupby(['year'])['positive','recovered','deaths'].sum().reset_index()
        res = res[res['year'].between(int(since),int(upto))]

        res['active'] = res['positive'] - res['recovered'] - res['deaths']
        res =Yearly(res.to_dict(orient="records"))

        return res

    def get_monthly_data(self, since = "2020.1" , upto = "nodata") -> Yearly:
        data = self.covid_driver.get_data_periodic()
        
        if upto == 'nodata' :
            upto = str(self.date_now.year) + "." + str(self.date_now.month)

        since = replace_fillz(since)
        upto = replace_fillz(upto)

        if  upto < since :
            return Monthly(values=[])

        res = data.groupby(['year','month'])['positive','recovered','deaths'].sum().reset_index()
        res['month'] = res['month'].astype(str).apply(lambda x: x.zfill(2))
        res['month'] = res[['year','month']].astype(str).agg('-'.join,axis=1)
        res = res.drop(columns=['year'])
        res = res[(res['month'] >= (since)) & (res['month'] <= (upto))]

        res['active'] = res['positive'] - res['recovered'] - res['deaths']
        
        res = Monthly(res.to_dict(orient="records"))

        return res


def replace_fillz(input : str) :
    val = input.split(".")
    val = val[0]+'-'+(val[1].zfill(2))
    
    return val