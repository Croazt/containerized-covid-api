import json
import requests
import pandas as pd
class CovidDataDriver:
    def __init__(self):
        self.init_data = self.init_data()
        self.data_total = self.init_data_total()

    def init_data(self):
        responses = requests.get(
            'https://data.covid19.go.id/public/api/update.json')
        return {'status_code': responses.status_code, 'data': json.dumps(responses.json())}

    def get_data(self):
        return self.init_data

    def init_data_total(self):
        data = json.loads(self.init_data['data'])

        data_total = {'total_positive': data['update']['total']['jumlah_positif'],
                      'total_recovered': data['update']['total']['jumlah_sembuh'],
                      'total_deaths': data['update']['total']['jumlah_meninggal'],
                      'total_active': data['update']['total']['jumlah_positif']-data['update']['total']['jumlah_sembuh']-data['update']['total']['jumlah_meninggal'],
                      'new_positive': data['update']['penambahan']['jumlah_positif'],
                      'new_recovered': data['update']['penambahan']['jumlah_sembuh'],
                      'new_active': data['update']['penambahan']['jumlah_positif'] - data['update']['penambahan']['jumlah_sembuh'] - data['update']['penambahan']['jumlah_meninggal'],
                      'new_deaths': data['update']['penambahan']['jumlah_meninggal']}

        return data_total

    def get_data_total(self):
        return self.data_total
