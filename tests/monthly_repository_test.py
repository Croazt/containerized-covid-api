import unittest
import json
import pandas as pd
import re
import datetime as dt

from src.driver.covid_data import CovidDataDriver
from src.repository.monthly_data_repository import MonthlyDataRepository, replace_fillz
from fastapi.testclient import TestClient
from src.domain.periodically_data import Monthly
from fastapi.testclient import TestClient

from app import app
class MonthlyDataRepositoryTest(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_monthly_object(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data()
        self.assertIsInstance(data, Monthly)

    def test_periodically_data_repository_given_string_returning_modified_string(self):
        word = replace_fillz('2020.1')
        pattern = re.compile("^[0-9][0-9][0-9][0-9].[0-9][0-9]")

        assert pattern.match(word)
        assert word == "2020-01"

    def test_periodically_data_repository_given_since_value_returns_Monthly_object_between_the_range_of_since_and_date_now(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since="2021.1")
        date = dt.datetime.now()
        monthup = str(date.year) + '-' + str(date.month).zfill(2)
        monthsin =  replace_fillz('2021.1')

        self.assertIsInstance(data, Monthly)
        assert data.values[0].month == monthsin
        assert data.values[-1].month == monthup

    def test_periodically_data_repository_given_since_and_value_returns_Monthly_object_between_the_range_of_since_and_upto(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since="2021.1", upto="2021.5")
        date = dt.datetime.now()
        
        monthup = replace_fillz('2021.5')
        monthsin = replace_fillz('2021.1')

        self.assertIsInstance(data, Monthly)
        assert data.values[0].month == monthsin
        assert data.values[-1].month == monthup
