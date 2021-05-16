import json

from typing import List, Union
import requests
from requests.models import HTTPError

from .exceptions import NotionException
from .constants import API_ENDPOINT, API_VERSION
from .types.errors import NotionError
from .types.users import User


class NotionClient:
    def __init__(self, token: str) -> None:
        self.users = UserEndpoint(token)


class UserEndpoint:
    def __init__(self, token) -> None:
        self.user_endpoint = f'{API_ENDPOINT}/users/'
        self.token = token

    def perform_request(self, method: str, endpoint: str):
        response = requests.request(
            method=method,
            url=endpoint,
            headers={
                'Authorization': f'Bearer {self.token}',
                'Notion-Version': API_VERSION
            }
        )

        try:
            response.raise_for_status()
        except HTTPError as e:
            raise NotionException(e.response.content)

        return response.json()

    def get(self, user_id: str) -> Union[User, NotionError]:
        endpoint = f'{self.user_endpoint}{user_id}'

        try:
            response = self.perform_request('GET', endpoint)
        except NotionException as e:
            return NotionError(e.code, e.message)

        return User(**response)

    def list(self) -> Union[List[User], NotionError]:
        endpoint = f'{self.user_endpoint}'

        try:
            response = self.perform_request('GET', endpoint)
        except NotionException as e:
            return NotionError(e.code, e.message)

        return [User(**item) for item in response['results']] 
