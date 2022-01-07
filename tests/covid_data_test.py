import unittest
import json
import pandas as pd
from src.driver.covid_data import CovidDataDriver
class TestCovidDataRequests(unittest.TestCase):
    def test_covid_data_fetch_returns_status_code_200(self):
        driver = CovidDataDriver()
        response = driver.get_data()
        assert response['status_code'] == 200

    def test_covid_data_fetch_returns_entityt_result_in_response(self):
        driver = CovidDataDriver()
        response = driver.get_data()
        assert len(json.loads(response['data'])) > 0
    
    
    def test_covid_data_extract_total_returns_dict(self) :
        driver = CovidDataDriver()
        data = (driver.get_data_total())

        print(data)
        self.assertIsInstance(data, dict)

