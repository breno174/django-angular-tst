import requests
from os import getenv


class MelhorEnvio(object):
    def __init__(self):
        self.url_api = getenv("API_URL")

    def call_api(self, path, data, method):
        url = f"{self.url_api}"

        headers = {"Content-Type": "application/json", "Bearer": getenv("API_TOKEN")}

        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, data=data)
            else:
                raise Exception("Invalid method")
        except Exception:
            raise Exception("Api consume dont work")
