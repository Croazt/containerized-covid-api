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
class MonthlyData(unittest.TestCase):
    def test_periodically_data_repository_given_empty_value_returns_monthly_object(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_monthly_data()
        self.assertIsInstance(data, Monthly)

    def test_periodically_data_repository_given_string_returning_modified_string(self):
        word = replace_fillz('2020.1')
        pattern = re.compile("^[0-9][0-9][0-9][0-9].[0-9][0-9]")

        assert pattern.match(word)
        assert word == "2020-01"

    def test_periodically_data_repository_given_since_value_returns_Monthly_object_between_the_range_of_since_and_date_now(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_monthly_data(since="2021.1")
        date = dt.datetime.now()
        monthup = str(date.year) + '-' + str(date.month).zfill(2)
        monthsin =  replace_fillz('2021.1')

        self.assertIsInstance(data, Monthly)
        assert data.values[0]['month'] == monthsin
        assert data.values[-1]['month'] == monthup

    def test_periodically_data_repository_given_since_and_value_returns_Monthly_object_between_the_range_of_since_and_upto(self):
        repository = MonthlyDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_monthly_data(since="2021.1", upto="2021.5")
        date = dt.datetime.now()
        
        monthup = replace_fillz('2021.5')
        monthsin = replace_fillz('2021.1')

        self.assertIsInstance(data, Monthly)
        assert data.values[0]['month'] == monthsin
        assert data.values[-1]['month'] == monthup

    def test_monthly_data_resource_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])

    def test_monthly_data_resource_given_since_value_return_dict_contain_data_range_since_to_month_now(self):
        with TestClient(app) as client:
            response = client.get('/monthly?since=2021.1')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])

    def test_monthly_data_resource_given_upto_value_return_dict_contain_data_range_upto_date_given(self):
        with TestClient(app) as client:
            response = client.get('/monthly?upto=2020.5')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])

    def test_monthly_data_resource_given_since_and_upto_value_return_dict_contain_data_range_since_to_upto(self):
        with TestClient(app) as client:
            response = client.get('/monthly?since=2019.1&upto=2021.1')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
    
    def test_yearly_data_resource_given_invalid_since_and_upto_value_return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly?since=aa&upto=aa')
            data = response.json()
            assert response.status_code == 422
            self.assertIsInstance(data, dict)

    def test_monthly_data_resource_given_years_param_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['month'].split('-')[0] == '2020'

    def test_monthly_data_resource_given_year_params_since_value_return_dict_contain_data_range_since_to_month_now(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020?since=1')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['month'].split('-')[0] == '2020'

    def test_monthly_data_resource_given_year_params_and_upto_value_return_dict_contain_data_range_upto_value_given(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020?upto=5')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['month'].split('-')[0] == '2020'

    def test_monthly_data_resource_given_year_params_since_and_upto_value_return_dict_contain_data_range_since_to_upto(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020?since=1&upto=6')
            data = response.json()
            assert ('month' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['month'].split('-')[0] == '2020'

    def test_monthly_data_resource_given_year_params_invalid_since_and_upto_value_return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020?since=aa&upto=aa')
            data = response.json()
            assert response.status_code == 422
            self.assertIsInstance(data, dict)

    def test_monthly_data_resource_given_year_and_month_params_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2020/5')
            data = response.json()
            assert response.status_code == 200
            self.assertIsInstance(data, dict)

    def test_monthly_data_resource_given_invalid_year_and_month_params__return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/monthly/2025/1')
            data = response.json()
            assert response.status_code == 204
            self.assertIsInstance(data, str)