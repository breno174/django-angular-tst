import requests
from os import getenv
from dotenv import load_dotenv
from .consumer import ConsumerUrlSerializer

load_dotenv()


class MelhorEnvio:
    @staticmethod
    def call_api(data, method):
        url_api = getenv("API_URL")
        path_serilizer = ConsumerUrlSerializer.create_path_by_body(data)
        url = f"{url_api}?{path_serilizer}"

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": getenv("API_TOKEN"),
            "User-Agent": "ReadMe-API-Explorer",
        }

        try:
            if method == "POST":
                response = requests.get(url, headers=headers)
                return response
            else:
                raise Exception("Invalid method")
        except Exception:
            raise Exception("Api consume dont work")
