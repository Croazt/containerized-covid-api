from src.interface.driver.covid_data import CovidDataDriverInt
from src.interface.repository.general_data_repository import GeneralDataRepository


class GeneralDataRepository(GeneralDataRepository):
    covid_driver: CovidDataDriverInt

    def __init__(self, covid_driver: CovidDataDriverInt):
        self.covid_driver = covid_driver

    def get_general_data(self) -> dict:
        res = self.covid_driver.get_data_total()
        return res