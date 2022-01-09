import unittest
import json
import pandas as pd
import re
import datetime as dt

from src.driver.covid_data import CovidDataDriver
from src.repository.periodically_data_repository import PeriodicallyDataRepository, replace_fillz
from fastapi.testclient import TestClient
from src.domain.periodically_data import Daily
from fastapi.testclient import TestClient

from app import app
class DailyData(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_daily_object(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_daily_data()
        self.assertIsInstance(data, Daily)
