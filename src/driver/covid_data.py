import json
import requests
class CovidDataDriver:
    def __init__(self) :
        self.init_data = self.init_data()

    def init_data(self):
        responses = requests.get('https://data.covid19.go.id/public/api/update.json')
        return {'status_code' : responses.status_code, 'data' : json.dumps(responses.json())}

        
    def get_data(self):
        return self.init_data