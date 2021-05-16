from dataclasses import dataclass, field
from typing import List, Literal, Union

from .misc import DateProperty
from .rich_text import RichText


@dataclass
class PageParent:
    type = Literal['database_id', 'page_id', 'workspace']
    database_id: str = None
    page_id: str = None


@dataclass
class SelectProperty:
    id: str
    name: str
    color: Literal[
        'default', 'gray', 'brown', 'red',
        'orange', 'yellow','green',
        'blue', 'purple', 'pink'
    ] = 'default'


@dataclass
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


@dataclass
class RelationProperty:
    id: str


@dataclass
class RollupProperty:
    type: Literal['number', 'date', 'array']

@dataclass
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


@dataclass
class Page:
    id: str
    created_time: str
    last_edited_time: str
    archived: bool
    parent: PageParent
    properties: Property
    object: str = 'page'

    def is_top_level_page(self) -> bool:
        return self.parent.type == 'workspace'

    def has_database_parent(self) -> bool:
        return self.parent.type == 'database_id'

    def has_page_parent(self) -> bool:
        return self.parent.type == 'page_id'