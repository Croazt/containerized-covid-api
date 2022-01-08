import unittest
import json
import pandas as pd

from src.driver.covid_data import CovidDataDriver
from src.repository.periodically_data_repository import PeriodicallyDataRepository
from fastapi.testclient import TestClient

from app import app
class PeriodicallyData(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_dictionary(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_yearly_data()
        self.assertIsInstance(data, dict)