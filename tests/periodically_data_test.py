import unittest
import json
import pandas as pd

from src.driver.covid_data import CovidDataDriver
from src.repository.periodically_data_repository import PeriodicallyDataRepository
from fastapi.testclient import TestClient
from src.domain.periodically_data import Yearly
from fastapi.testclient import TestClient

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

    def test_periodically_data_repository_given_since_and_upto_value_returns_Yearly_object_between_the_range_of_since_and_upto(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_yearly_data(since="2021",upto='2024')
        self.assertIsInstance(data, Yearly)
        assert data.values[0]['year'] == 2021

    def test_periodically_data_repository_given_since_value_that_more_than_upto_value_returns_Empty_Yearly_object(self):
        repository = PeriodicallyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_yearly_data(since="2025",upto='2024')
        self.assertIsInstance(data, Yearly)
        assert data.values == []

    def test_periodically_data_resource_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/yearly')
            data = response.json()
            assert ('year' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])

    def test_periodically_data_resource_given_since_value_return_dict_contain_data_range_since_to_year_now(self):
        with TestClient(app) as client:
            response = client.get('/yearly?since=2021')
            data = response.json()
            assert ('year' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])