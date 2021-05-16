from dataclasses import dataclass, field
from typing import Dict, Literal


@dataclass
class HumanInformation:
    email: str


@dataclass
class User:
    id: str
    type: Literal['person', 'bot']
    person: HumanInformation = None
    bot: Dict = field(default_factory=dict)
    object: str = 'user'
    name: str = ''
    avatar: str = ''

    def is_bot(self):
        return self.type == 'bot'