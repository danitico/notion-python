import json
from dataclasses import asdict
from typing import Dict, List, Optional, Tuple, Union

import requests
from requests.models import HTTPError

from .exceptions import NotionException
from .constants import API_ENDPOINT, API_VERSION
from .types.database import Database
from .types.errors import NotionError
from .types.misc import QueryParams
from .types.page import Page
from .types.users import User


class NotionClient:
    def __init__(self, token: str) -> None:
        self.users = UserEndpoint(token)
        self.databases = DatabaseEndpoint(token)


class GenericEndpoint:
    def perform_request(self, request_data: Dict) -> Dict:
        response = requests.request(**request_data)

        try:
            response.raise_for_status()
        except HTTPError as e:
            raise NotionException(e.response.content)

        return response.json()

class DatabaseEndpoint(GenericEndpoint):
    def __init__(self, token: str) -> None:
        self.database_endpoint: str = f'{API_ENDPOINT}/databases/'
        self.token: str = token

    def get(self, database_id: str) -> Union[Database, NotionError]:
        request_data = {
            'method': 'GET',
            'url': f'{self.database_endpoint}{database_id}',
            'headers': {
                'Authorization': f'Bearer {self.token}',
                'Notion-Version': API_VERSION
            }
        }

        try:
            response = self.perform_request(request_data)
        except NotionException as e:
            return NotionError(e.code, e.message)

        return Database(**response)

    def list(self, query_params: QueryParams) -> Union[Tuple[List[Database],Optional[str]], NotionError]:
        request_data = {
            'method': 'GET',
            'url': f'{self.database_endpoint}',
            'params': asdict(query_params),
            'headers': {
                'Authorization': f'Bearer {self.token}',
                'Notion-Version': API_VERSION
            }
        }

        try:
            response = self.perform_request(request_data)
        except NotionException as e:
            return NotionError(e.code, e.message)

        next_cursor = response['next_cursor'] if response['has_more'] else None

        return [Database(**item) for item in response['results']], next_cursor

    def query(self, query_params: QueryParams) -> Union[Tuple[List[Page], Optional[str]], NotionError]:
        pass


class UserEndpoint(GenericEndpoint):
    def __init__(self, token) -> None:
        self.user_endpoint = f'{API_ENDPOINT}/users/'
        self.token = token

    def get(self, user_id: str) -> Union[User, NotionError]:
        request_data = {
            'method': 'GET',
            'url': f'{self.user_endpoint}{user_id}',
            'headers': {
                'Authorization': f'Bearer {self.token}',
                'Notion-Version': API_VERSION
            }
        }

        try:
            response = self.perform_request(request_data)
        except NotionException as e:
            return NotionError(e.code, e.message)

        return User(**response)

    def list(self, query_params: QueryParams) -> Union[Tuple[List[User],Optional[str]], NotionError]:
        request_data = {
            'method': 'GET',
            'url': f'{self.user_endpoint}',
            'params': asdict(query_params),
            'headers': {
                'Authorization': f'Bearer {self.token}',
                'Notion-Version': API_VERSION
            }
        }

        try:
            response = self.perform_request(request_data)
        except NotionException as e:
            return NotionError(e.code, e.message)

        next_cursor = response['next_cursor'] if response['has_more'] else None

        return [User(**item) for item in response['results']], next_cursor
