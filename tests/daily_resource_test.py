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
class DailyDataResourceTest(unittest.TestCase):
    def test_daily_data_resource_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
    
    def test_daily_data_resource_given_since_value_return_dict_contain_data_range_since_to_month_now(self):
        with TestClient(app) as client:
            response = client.get('/daily?since=2021.1.1')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
    
    def test_daily_data_resource_given_upto_value_return_dict_contain_data_range_since_to_month_now(self):
        with TestClient(app) as client:
            response = client.get('/daily?upto=2021.1.1')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
    
    def test_daily_data_resource_given_since_and_upto_value_return_dict_contain_data_range_since_to_upto(self):
        with TestClient(app) as client:
            response = client.get('/daily?since=2019.1.2&upto=2021.1.3')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
    
    def test_daily_data_resource_given_invalid_since_and_upto_value_return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily?since=aa&upto=aa')
            data = response.json()
            assert response.status_code == 422
            self.assertIsInstance(data, dict)

    def test_daily_data_resource_given_years_param_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2020')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] == '2020'

    def test_daily_data_resource_given_year_params_since_value_return_dict_contain_data_range_since_to_date_now(self):
        with TestClient(app) as client:
            response = client.get('/daily/2020?since=1.2')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] == '2020'
    
    
    def test_daily_data_resource_given_year_params_since_value_return_dict_contain_data_range_to_upto(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021?upto=1.2')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] == '2021'

    def test_daily_data_resource_given_year_params_since_value_return_dict_contain_data_range_since_to_upto(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021?since=1.2&upto=5.2')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] == '2021'

    def test_daily_data_resource_given_year_params_invalid_since_and_upto_value_return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2020?since=aa&upto=aa')
            data = response.json()
            assert response.status_code == 422
            self.assertIsInstance(data, dict)
            
    def test_daily_data_resource_given_year_and_month_params_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021/5')
            data = response.json()
            assert response.status_code == 200
            self.assertIsInstance(data, dict)
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] +'-' +data['data'][0]['date'].split('-')[1]  == '2021-05'
    
    def test_daily_data_resource_given_invalid_year_and_month_params__return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2025/1')
            data = response.json()
            assert response.status_code == 400
            self.assertIsInstance(data, dict)
            assert data['data'] == {}

    def test_daily_data_resource_given_year_month_params_with_since_value_return_dict_contain_data_range_since_to_date_now(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021/5?since=1')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] +'-' +data['data'][0]['date'].split('-')[1]  == '2021-05'

    def test_daily_data_resource_given_year_month_params_with_upto_value_return_dict_contain_data_range_since_to_date_now(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021/5?upto=4')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] +'-' +data['data'][0]['date'].split('-')[1]  == '2021-05'
    
    def test_daily_data_resource_given_year_month_params_with_since_and_upto_value_return_dict_contain_data_range_since_to_date_now(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021/5?since=3&upto=4')
            data = response.json()
            assert ('date' in data['data'][0]) and ('positive' in data['data'][0]) and ('recovered' in data['data'][0]) and ('deaths' in data['data'][0])
            assert data['data'][0]['date'].split('-')[0] +'-' +data['data'][0]['date'].split('-')[1]  == '2021-05'
    
    def test_daily_data_resource_given_year_month_params_with_invalid_since_and_upto_value_return_dict_contain_data_range_since_to_date_now(self):
        with TestClient(app) as client:
            response = client.get('/daily/2021/5?since=ss&upto=dd')
            data = response.json()
            assert response.status_code == 422
            self.assertIsInstance(data, dict)
    
    def test_daily_data_resource_given_year_month_and_day_params_return_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2020/5/2')
            data = response.json()
            assert response.status_code == 200
            self.assertIsInstance(data, dict)
            assert data['data']['date']  == '2020-05-02'

    def test_daily_data_resource_given_invalid_year_month_and_day_params_return_empty_dict(self):
        with TestClient(app) as client:
            response = client.get('/daily/2025/1/2')
            data = response.json()
            assert response.status_code == 400
            self.assertIsInstance(data, dict)
            assert data['data'] == {}