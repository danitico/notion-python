from dataclasses import dataclass
from typing import List, Literal, Sequence, Union

from .misc import Date
from .users import User


@dataclass
class Annotation:
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: Literal[
        'default', 'gray', 'brown', 'orange',
        'yellow', 'green', 'blue', 'purple',
        'pink', 'red', 'gray_background', 'brown_background',
        'orange_background', 'yellow_background', 'green_background', 'blue_background',
        'purple_background', 'pink_background', 'red_background'
    ]


@dataclass
class Link:
    url: str
    type: str = 'url'


@dataclass
class Text:
    content: str
    link: Link = None

@dataclass
class PageMention:
    id: str


@dataclass
class DatabaseMention:
    id: str


@dataclass
class Mention:
    type: Literal['user', 'page', 'database', 'date']
    user: User = None
    page: PageMention = None
    database: DatabaseMention = None
    date: Date = None

    def is_user_mention(self) -> bool:
        return self.type == 'user'

    def is_page_mention(self) -> bool:
        return self.type == 'page'

    def is_database_mention(self) -> bool:
        return self.type == 'database'

    def is_date_mention(self) -> bool:
        return self.type == 'date'


@dataclass
class Equation:
    expression: str


@dataclass
class RichText:
    plain_text: str
    annotations: Annotation
    type: Literal['text', 'mention', 'equation']
    text: Text = None
    mention: Mention = None
    equation = Equation = None
    href: str = ''

    def is_text(self) -> bool:
        return self.type == 'text'

    def is_mention(self) -> bool:
        return self.type == 'mention'

    def is_equation(self) -> bool:
        return self.type == 'equation'
