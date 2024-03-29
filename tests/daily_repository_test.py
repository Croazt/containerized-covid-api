import unittest
import json
import pandas as pd
import re
import datetime as dt

from src.driver.covid_data import CovidDataDriver
from src.repository.daily_data_repository import DailyDataRepository, concatenate_date, replace_fillz
from fastapi.testclient import TestClient
from src.domain.periodically_data import Daily
from fastapi.testclient import TestClient

from app import app
class DailyDataRepositoryTest(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_daily_object(self):
        repository = DailyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data()
        self.assertIsInstance(data, Daily)

    def test_periodically_data_repository_given_since_value_returns_Daily_object_between_the_range_of_since_and_date_now(self):
        repository = DailyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since="2021.1.1")
        dates = dt.datetime.now()

        monthup = replace_fillz(concatenate_date(dates.year, dates.month, dates.day))
        monthup_yest = replace_fillz(concatenate_date(dates.year, dates.month, dates.day -1))
        monthsin = replace_fillz('2021.1.1')
        
        self.assertIsInstance(data, Daily)
        assert data.values[0].date == (monthsin)
        assert data.values[-1].date == str(monthup) or data.values[-1]['date'] == str(monthup_yest)

    def test_periodically_data_repository_given_since_and_upto_value_returns_Daily_object_between_the_range_of_since_and_upto(self):
        repository = DailyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since="2021.1.3", upto="2021.4.5")
        date = dt.datetime.now()
        
        monthup = replace_fillz('2021.4.5')
        monthsin = replace_fillz('2021.1.3')
        
        self.assertIsInstance(data, Daily)
        assert data.values[0].date == str(monthsin)
        assert data.values[-1].date == str(monthup)