import requests
from os import getenv
from .consumer import ConsumerUrlSerializer


class MelhorEnvio:
    def __init__(self):
        self.url_api: str = getenv("API_URL")

    @staticmethod
    def call_api(data, method):
        path_serilizer = ConsumerUrlSerializer.create_path_by_body(data)
        url = f"{MelhorEnvio.url_api}?{path_serilizer}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": getenv("API_TOKEN"),
            "User-Agent": "ReadMe-API-Explorer",
        }

        try:
            if method == "POST":
                response = requests.get(url, headers=headers)
            else:
                raise Exception("Invalid method")
        except Exception:
            raise Exception("Api consume dont work")
