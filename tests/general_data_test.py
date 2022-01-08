import unittest
import json
import pandas as pd

from src.driver.covid_data import CovidDataDriver
from src.repository.general_data_repository import GeneralDataRepository
from fastapi.testclient import TestClient

from app import app
class GeneralData(unittest.TestCase):
    def test_general_data_repository_returns_dictionary(self):
        repository = GeneralDataRepository(covid_driver=CovidDataDriver())
        data = repository.get_general_data()
        self.assertIsInstance(data, dict)

    def test_general_data_resource_returns_result_in_response(self):
        with TestClient(app) as client:
            response = client.get('/')
            data = response.json()
            assert ('total_positive' in data['data']) and ('total_recovered' in data['data']) and ('total_deaths' in data['data']) and ('total_active' in data['data'])