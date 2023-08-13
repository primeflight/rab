import json
from urllib.request import urlopen


class Search:
    def __init__(self):
        self.json_data = None
        self.cache = {}

    def update_data(self):
        json_url = "https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/dados_aeronaves.json"
        response = urlopen(json_url)
        data = response.read()
        encoding = response.info().get_content_charset("utf-8-sig")
        self.json_data = json.loads(data.decode(encoding))

    def aircraft(self, prefix):
        if self.json_data is None:
            self.update_data()

        if prefix in self.cache:
            return self.cache[prefix]

        filtered_aircraft = [
            aircraft for aircraft in self.json_data if aircraft["MARCA"] == prefix
        ]

        self.cache[prefix] = filtered_aircraft
        return filtered_aircraft

    def get_data(self):
        if self.json_data is None:
            self.update_data()

        return self.json_data
