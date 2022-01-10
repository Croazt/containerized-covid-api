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
class MonthlyDataResourceTest(unittest.TestCase):
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
            assert response.status_code == 400
            self.assertIsInstance(data, dict)
            assert data['data'] == {}