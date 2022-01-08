import unittest
import json
from fastapi.testclient import TestClient

from app import app

class TestRoot(unittest.TestCase):

    def test_root_endpoint_returns_200(self):
        with TestClient(app) as client:
            response = client.get('/')
            assert response.status_code == 200

    def test_root_endpoint_returns_general_data_result_in_response(self):
        with TestClient(app) as client:
            response = client.get('/')
            data = response.json()
            assert ('total_positive' in data['data']) and ('total_recovered' in data['data']) and ('total_deaths' in data['data']) and ('total_active' in data['data'])