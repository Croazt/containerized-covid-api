import unittest
import json
from flask import request

from app import app

class TestRoot(unittest.TestCase):
    def test_root_endpoint_returns_200(self):
        with app.test_client() as client:
            response = client.get('/')
            assert response._status_code == 200