import unittest
import json
import pandas as pd

from src.driver.covid_data import CovidDataDriver
from src.repository.yearly_data_repository import YearlyDataRepository, replace_fillz
from fastapi.testclient import TestClient
from src.domain.periodically_data import Yearly
from fastapi.testclient import TestClient

from app import app
class YearlyDataRepositoryTest(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_Yearly_object(self):
        repository = YearlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data()
        self.assertIsInstance(data, Yearly)

    def test_periodically_data_repository_given_since_value_returns_Yearly_object_between_the_range_of_since_and_date_now(self):
        repository = YearlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since=2021)
        self.assertIsInstance(data, Yearly)
        assert data.values[0].year == "2021"

    def test_periodically_data_repository_given_since_and_upto_value_returns_Yearly_object_between_the_range_of_since_and_upto(self):
        repository = YearlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since=2021,upto=2024)
        self.assertIsInstance(data, Yearly)
        assert data.values[0].year == "2021"

    def test_periodically_data_repository_given_since_value_that_more_than_upto_value_returns_Empty_Yearly_object(self):
        repository = YearlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_data(since=2025,upto=2024)
        self.assertIsInstance(data, Yearly)
        assert data.values == []