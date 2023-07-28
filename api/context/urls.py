import requests

class MelhorEnvio(object):
    def __init__(self):
        self.url_api = 'https://melhorenvio.com.br/api/v2/'

    def call_api(self, path, data, method):
        url = f"{self.url_api}/{path}"

        headers = {
            'Content-Type': 'application/json',
            "Bearer": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImEzZWFiNTQ5MmU0M2Q1ZjIwZDY1NTk2MGNhNmU5NWQyMWQ5YjFiOGYwMDI2ZWJkMzA5OGI0NWViM2RmNGUwNzk4ZTU5NzMwMWMyMzJlMDdiIn0.eyJhdWQiOiI5NTYiLCJqdGkiOiJhM2VhYjU0OTJlNDNkNWYyMGQ2NTU5NjBjYTZlOTVkMjFkOWIxYjhmMDAyNmViZDMwOThiNDVlYjNkZjRlMDc5OGU1OTczMDFjMjMyZTA3YiIsImlhdCI6MTY4MDEwMjAwMCwibmJmIjoxNjgwMTAyMDAwLCJleHAiOjE3MTE3MjQ0MDAsInN1YiI6IjMxODg1OTMwLTYzZWUtNDAxOS04NWFiLTM4ZDRiODdkOTk2NyIsInNjb3BlcyI6WyJjYXJ0LXJlYWQiLCJjYXJ0LXdyaXRlIiwiY29tcGFuaWVzLXJlYWQiLCJjb21wYW5pZXMtd3JpdGUiLCJjb3Vwb25zLXJlYWQiLCJjb3Vwb25zLXdyaXRlIiwibm90aWZpY2F0aW9ucy1yZWFkIiwib3JkZXJzLXJlYWQiLCJwcm9kdWN0cy1yZWFkIiwicHJvZHVjdHMtZGVzdHJveSIsInByb2R1Y3RzLXdyaXRlIiwicHVyY2hhc2VzLXJlYWQiLCJzaGlwcGluZy1jYWxjdWxhdGUiLCJzaGlwcGluZy1jYW5jZWwiLCJzaGlwcGluZy1jaGVja291dCIsInNoaXBwaW5nLWNvbXBhbmllcyIsInNoaXBwaW5nLWdlbmVyYXRlIiwic2hpcHBpbmctcHJldmlldyIsInNoaXBwaW5nLXByaW50Iiwic2hpcHBpbmctc2hhcmUiLCJzaGlwcGluZy10cmFja2luZyIsImVjb21tZXJjZS1zaGlwcGluZyIsInRyYW5zYWN0aW9ucy1yZWFkIiwidXNlcnMtcmVhZCIsInVzZXJzLXdyaXRlIiwid2ViaG9va3MtcmVhZCIsIndlYmhvb2tzLXdyaXRlIl19.PTb06vQtUANuSa246Atljh7_OUbs7y0nmd1ARStq7PCgKSQCQ6MSaZSsRoSJ6P60EXOqSMndmiRVXfjz8c8sXW0L-cLjmuRM8mvG1DZ9VtfgLUmNd7pc-5kVpJh91ICVoQE7AQjXJkQkS3NdyJYr4HoMLlfNmuwJZGQUOpM2SS-SotXHP2zDMU43J61gjd3D-0Mcv_rVKpq46FAK5ZPfZlEE5e8ednepRY7EtVrM9XmVnVl771yUnKtE7DVvtCCpFIc2YfkCTNHLyGasG9wPCfoyXPZd5zBqsEIKJz2sbyoXrAIRdSUScoH-eD4ulLFH_z93-ej2Py8X6LogPfaIqE7RzEFyl4ZLNvdABjn7dQ1edcWbA8xQu8lMIFSdkwSBbcJ_JsNVFWlnh25DTcLItzaKF9mRSZuBmKQCz5xVuomGFQmX3ucw2uyTyoC3PItRhDQbDDhaY11IECyMbvy--nr3HhTzf2n3JpUsCFMk8vZwifvS0G6Xip_AtHqBDYiIrJXJOo4phybBLzuKw3E4SCm78AJsJAAWOkw4Y_nACF0K4l3hdrchpLPOsGA3Twi3oVIo6CM41SCC0orvfShGeRUOX1jCYxa63rkiQC1qlg-FnI3_aHrML01XI4wTHf-QS_MEXWNl8rQtmEYUkZBqcS5LTV0-wb3FHi691FwlD9A"
        }

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=data)
            else:
                raise Exception('Invalid method')
        except Exception:
            raise Exception("Api consume dont work")
