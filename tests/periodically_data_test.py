import unittest
import json
import pandas as pd

from src.driver.covid_data import CovidDataDriver
from src.repository.periodically_data_repository import PeriodicallyDataRepository
from fastapi.testclient import TestClient
from src.domain.periodically_data import Yearly

from app import app
class PeriodicallyData(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_Yearly_object(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_yearly_data()
        self.assertIsInstance(data, Yearly)

    def test_periodically_data_repository_given_since_value_returns_Yearly_object_between_the_range_of_since_and_date_now(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_yearly_data(since="2021")
        self.assertIsInstance(data, Yearly)
        assert data.values[0]['year'] == 2021