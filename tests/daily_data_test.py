import unittest
import json
import pandas as pd
import re
import datetime as dt

from src.driver.covid_data import CovidDataDriver
from src.repository.periodically_data_repository import PeriodicallyDataRepository, concatenate_date, replace_fillz
from fastapi.testclient import TestClient
from src.domain.periodically_data import Daily
from fastapi.testclient import TestClient

from app import app
class DailyData(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_daily_object(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_daily_data()
        self.assertIsInstance(data, Daily)

    def test_periodically_data_repository_given_since_value_returns_Daily_object_between_the_range_of_since_and_date_now(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_daily_data(since="2021.1.1")
        dates = dt.datetime.now()

        monthup = replace_fillz(concatenate_date(dates.year, dates.month, dates.day))
        monthsin = replace_fillz('2021.1.1')
        
        self.assertIsInstance(data, Daily)
        assert data.values[0]['date'] == monthsin
        assert data.values[-1]['date'] == monthup

    def test_periodically_data_repository_given_since_and_upto_value_returns_Daily_object_between_the_range_of_since_and_upto(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_daily_data(since="2021.1.3", upto="2021.4.5")
        date = dt.datetime.now()
        
        monthup = replace_fillz('2021.4.5')
        monthsin = replace_fillz('2021.1.3')
        
        self.assertIsInstance(data, Daily)
        assert data.values[0]['date'] == monthsin
        assert data.values[-1]['date'] == monthup