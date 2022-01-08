import unittest
import json
import pandas as pd
from src.driver.covid_data import CovidDataDriver
from src.repository.general_data_repository import GeneralDataRepository

class GeneralData(unittest.TestCase):
    def test_general_data_repository_returns_dictionary(self):
        repository = GeneralDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_general_data()
        self.assertIsInstance(data, dict)
