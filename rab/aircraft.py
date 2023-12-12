import json
from urllib.request import urlopen
import os
from datetime import datetime


class Search:
    def __init__(self):
        self.json_data = None
        self.cache = {}
        self.local_directory = "dados_aeronaves"
        self.file_extension = ".json"

    def get_local_filename(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        return os.path.join(self.local_directory, current_date + self.file_extension)

    def update_data(self):
        local_filename = self.get_local_filename()

        if os.path.exists(local_filename):
            with open(local_filename, "r", encoding="utf-8") as file:
                self.json_data = json.load(file)
        else:
            json_url = (
                "https://sistemas.anac.gov.br/dadosabertos/Aeronaves/RAB/dados_aeronaves.json"
            )
            response = urlopen(json_url)
            data = response.read()
            encoding = response.info().get_content_charset("utf-8-sig")
            self.json_data = json.loads(data.decode(encoding))

            for filename in os.listdir(self.local_directory):
                file_path = os.path.join(self.local_directory, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"Erro ao excluir {file_path}: {e}")

            os.makedirs(self.local_directory, exist_ok=True)
            with open(local_filename, "w", encoding="utf-8") as file:
                json.dump(self.json_data, file, ensure_ascii=False, indent=4)

    def aircraft(self, prefix):
        if self.json_data is None:
            self.update_data()

        if prefix in self.cache:
            return self.cache[prefix]

        filtered_aircraft = [aircraft for aircraft in self.json_data if aircraft["MARCA"] == prefix]

        self.cache[prefix] = filtered_aircraft
        return filtered_aircraft

    def get_data(self):
        if self.json_data is None:
            self.update_data()

        return self.json_data
