import json
import requests
import pandas as pd


class CovidDataDriver:
    def __init__(self):
        self.init_data = self.init_data()
        self.data_total = self.init_data_total()
        self.data_periodic = self.init_data_periodic()

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

    def init_data_periodic(self):
        data = json.loads(self.init_data['data'])['update']['harian']

        df_data_periodic = pd.DataFrame(
            columns=['key', 'positive', 'recovered', 'deaths'])
        d = {}

        i = 0
        for data_daily in data:
            d[i] = {'key': data_daily['key'], 'positive': data_daily['jumlah_positif']['value'], 'recovered':  data_daily['jumlah_sembuh']
                    ['value'], 'deaths': data_daily['jumlah_meninggal']['value']}
            i = i+1

        df_data_periodic = df_data_periodic.from_dict(d,orient="index")
        key = pd.to_datetime(df_data_periodic['key'], unit='ms')
        
        df_data_periodic = df_data_periodic.join(pd.DataFrame({'year' : key.dt.year}))
        df_data_periodic = df_data_periodic.join(pd.DataFrame({'month' : key.dt.month}))
        df_data_periodic = df_data_periodic.join(pd.DataFrame({'date' : key.dt.day}))

        return df_data_periodic

    def get_data_periodic(self):
        return self.data_periodic
