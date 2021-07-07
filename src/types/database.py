from typing import List, Literal

from .dataclass import nested_dataclass
from .rich_text import RichText


@nested_dataclass
class NumberProperty:
    format: Literal[
        'number', 'number_with_commas', 'percent', 'dollar', 'euro',
        'pound', 'yen', 'ruble', 'rupee', 'won', 'yuan'
    ]

@nested_dataclass
class SelectOptionObject:
    name: str
    id: str
    color: Literal[
        'default', 'gray', 'brown', 'orange',
        'yellow', 'green', 'blue',
        'purple', 'pink', 'red'
    ]


@nested_dataclass
class SelectProperty:
    options: List[SelectOptionObject]


@nested_dataclass
class FormulaProperty:
    expression: str


@nested_dataclass
class RelationProperty:
    database_id: str
    synced_property_name: str = None
    synced_property_id: str = None

class RollupProperty:
    relation_property_name: str
    relation_property_id: str
    rollup_property_name: str
    rollup_property_id: str
    function: Literal[
        'count_all', 'count_values', 'count_unique_values',
        'count_empty', 'count_not_empty', 'percent_empty',
        'percent_not_empty', 'sum', 'average', 'median',
        'min', 'max', 'range'
    ]


@nested_dataclass
class DatabaseProperty:
    id: str
    type: Literal[
        'rich_text', 'number', 'select', 'multi_select',
        'date', 'formula', 'relation', 'rollup',
        'title', 'people', 'files', 'checkbox',
        'url', 'email', 'phone_number', 'created_time', 
        'created_by', 'last_edited_time', 'last_edited_by'
    ]
    number: NumberProperty = None
    select: SelectProperty = None
    multi_select: SelectProperty = None
    formula: FormulaProperty = None
    relation: RelationProperty = None
    rollup: RollupProperty = None


@nested_dataclass
class KeyValueObject:
    key: str
    value: DatabaseProperty


@nested_dataclass
class Database:
    id: str
    created_time: str
    last_edited_time: str
    title: List[RichText]
    properties: List[KeyValueObject]
    object: str = 'database'

