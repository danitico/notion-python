from dataclasses import field
from typing import Dict, List, Literal, Union

from .dataclass import nested_dataclass
from .misc import DateProperty
from .rich_text import RichText
from .users import User


@nested_dataclass
class PageParent:
    type = Literal['database_id', 'page_id', 'workspace']
    database_id: str = None
    page_id: str = None


@nested_dataclass
class SelectProperty:
    id: str
    name: str
    color: Literal[
        'default', 'gray', 'brown', 'red',
        'orange', 'yellow','green',
        'blue', 'purple', 'pink'
    ] = 'default'


@nested_dataclass
class FormulaProperty:
    type: Literal['string', 'number', 'boolean', 'date']
    string: str = None
    number: Union[int, float] = None
    boolean: bool = None
    date: DateProperty = None

    def is_string_formula(self):
        return self.type == 'string'

    def is_number_formula(self):
        return self.type == 'number'
    
    def is_boolean_formula(self):
        return self.type == 'boolean'

    def is_date_formula(self):
        return self.type == 'date'


@nested_dataclass
class RelationProperty:
    id: str


@nested_dataclass
class RollupProperty:
    type: Literal['number', 'date', 'array']
    number: Union[int, float] = None
    date: DateProperty = None
    array: List[Dict] = field(default_factory=list)

@nested_dataclass
class FileProperty:
    name: str


@nested_dataclass
class TitleProperty:
    title: List[RichText] = field(default_factory=list)


@nested_dataclass
class KeyValueObject:
    key: str
    value: Union[int, float]


@nested_dataclass
class Property:
    id: str
    type: Literal[
        'rich_text', 'number', 'select', 'multi_select',
        'date', 'formula', 'relation', 'rollup',
        'title', 'people', 'files', 'checkbox',
        'url', 'email', 'phone_number', 'created_time', 
        'created_by', 'last_edited_time', 'last_edited_by'
    ]
    title: List[RichText] = field(default_factory=list)
    rich_text: List[RichText] = field(default_factory=list)
    number: Union[int, float] = None
    select: SelectProperty = None
    multi_select: List[SelectProperty] = field(default_factory=list)
    date: DateProperty = None
    formula: FormulaProperty = None
    relation: List[RelationProperty] = field(default_factory=list)
    rollup: RollupProperty = None
    people: List[User] = field(default_factory=list)
    files: List[FileProperty] = field(default_factory=list)
    checkbox: bool = None
    url: str = None
    email: str = None
    phone_number: str = None
    created_time: str = None
    created_by: User = None
    last_edited_time: str = None
    last_edited_by: User = None


@nested_dataclass
class Page:
    id: str
    created_time: str
    last_edited_time: str
    archived: bool
    parent: PageParent
    properties: Union[List[KeyValueObject], TitleProperty]
    object: str = 'page'

    def is_top_level_page(self) -> bool:
        return self.parent.type == 'workspace'

    def has_database_parent(self) -> bool:
        return self.parent.type == 'database_id'

    def has_page_parent(self) -> bool:
        return self.parent.type == 'page_id'
