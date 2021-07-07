import json


class NotionException(Exception):
    def __init__(self, response) -> None:
        response_json = json.loads(response.decode('utf-8'))

        self.code = response_json['code']
        self.message = response_json['message']