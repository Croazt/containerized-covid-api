import unittest
import json
import pandas as pd
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
    
    total_df_template = pd.DataFrame(columns=['total_positive', 'total_recovered', 'total_deaths', 'total_active', 'new_positive', 'new_recovered', 'new_deaths', 'new_active'])

    def test_covid_data_extract_total_returns_dataframe(self) :
        driver = CovidDataDriver()
        data = data.get_data_total()
        pd.testing.assert_frame_equal(total_df_template, data)

