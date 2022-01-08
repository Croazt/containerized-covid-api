import unittest
import json
from flask import request

from app import app

class TestRoot(unittest.TestCase):
    def test_root_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.get('/')
            assert response._status_code == 200

    def test_root_endpoint_returns_general_data_result_in_response(self):
        with app.test_client() as client:
            response = client.get('/')
            data = json.loads(response.get_data())
            assert ('total_positive' in data['data']) and ('total_recovered' in data['data'][0]) and ('total_deaths' in data['data'][0]) and ('total_active' in data['data'][0])