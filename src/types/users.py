from dataclasses import field
from typing import Dict, Literal

from .dataclass import nested_dataclass


@nested_dataclass
class HumanInformation:
    email: str


@nested_dataclass
class User:
    id: str
    type: Literal['person', 'bot']
    person: HumanInformation = None
    bot: Dict = field(default_factory=dict)
    object: str = 'user'
    name: str = ''
    avatar_url: str = ''

    def is_bot(self):
        return self.type == 'bot'