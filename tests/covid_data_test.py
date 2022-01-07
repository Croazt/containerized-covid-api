import unittest
import json
from src.driver.covid_data import CovidDataDriver
class TestCovidDataRequests(unittest.TestCase):

    def test_covid_data_fetch_returns_status_code_200(self):
        data = CovidDataDriver()
        response = data.get_data()
        assert response['status_code'] == 200

    def test_covid_data_fetch_returns_entityt_result_in_response(self):
        data = CovidDataDriver()
        response = data.get_data()
        assert len(json.loads(response['data'])) > 0