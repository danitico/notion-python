from dataclasses import dataclass, field
from typing import Dict, List, Literal, Type, Union

from .dataclass import nested_dataclass


@dataclass
class Sort:
    """
        Sort objects describe the order of database query results

        property (str): The name of the property to sort against.
        timestamp (Literal['created_time', 'last_edited_time']): The name of the timestamp to sort against. Possible values include "created_time" and "last_edited_time".
        direction (Literal['ascending', 'descending']): The direction to sort. Possible values include "ascending" and "descending".
    """

    property: str
    timestamp: Literal['created_time', 'last_edited_time']
    direction: Literal['ascending', 'descending']


@dataclass
class TextFilterCondition:
    """ 
        A text filter condition applies to database properties of types "title", "rich_text", "url", "email", and "phone"

            property (str): Property name
            equals (str): Only return pages where the page property value matches the provided value exactly.
            does_not_equal (str): Only return pages where the page property value does not match the provided value exactly.
            contains (str): Only return pages where the page property value contains the provided value.
            does_not_contain (str): Only return pages where the page property value does not contain the provided value.
            starts_with (str): Only return pages where the page property value starts with the provided value.
            ends_with (str): Only return pages where the page property value ends with the provided value.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    equals: str = None
    does_not_equal: str = None
    contains: str = None
    does_not_contain: str = None
    starts_with: str = None
    ends_with: str = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class NumberFilterCondition:
    """ 
        A number filter condition applies to database properties of type "number"

            property (str): Property name
            equals (Union[int, float]): Only return pages where the page property value matches the provided value exactly.
            does_not_equal (Union[int, float]): Only return pages where the page property value does not match the provided value exactly.
            greater_than (Union[int, float]): Only return pages where the page property value is greater than the provided value.
            less_than (Union[int, float]): Only return pages where the page property value is less than the provided value.
            greater_than_or_equal_to (Union[int, float]): Only return pages where the page property value is greater than or equal to the provided value.
            less_than_or_equal_to (Union[int, float]): Only return pages where the page property value is less than or equal to the provided value.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    equals: Union[int, float] = None
    does_not_equal: Union[int, float] = None
    greater_than: Union[int, float] = None
    less_than: Union[int, float] = None
    greater_than_or_equal_to: Union[int, float] = None
    less_than_or_equal_to: Union[int, float] = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class CheckboxFilterCondition:
    """ 
        A checkbox filter condition applies to database properties of type "checkbox"

            property (str): Property name
            equals (bool): Only return pages where the page property value matches the provided value exactly.
            does_not_equal (bool): Only return pages where the page property value does not match the provided value exactly.
    """

    property: str
    equals: bool = None
    does_not_equal: bool = None


@dataclass
class SelectFilterCondition:
    """ 
        A select filter condition applies to database properties of type "select"

            property (str): Property name
            equals (str): Only return pages where the page property value matches the provided value exactly.
            does_not_equal (str): Only return pages where the page property value does not match the provided value exactly.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    equals: str = None
    does_not_equal: str = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class MultiSelectFilterCondition:
    """
        A select filter condition applies to database properties of type "multi_select"

            property (str): Property name
            equals (str): Only return pages where the page property value matches the provided value exactly.
            does_not_equal (str): Only return pages where the page property value does not match the provided value exactly.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    equals: str = None
    does_not_equal: str = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class DateFilterCondition:
    """
        A date filter condition applies to database properties of types "date", "created_time", and "last_edited_time"

            property (str): Property name
            equals (ISO 8601 date and time): Only return pages where the page property value matches the provided date exactly. Note that the comparison is done against the date. Any time information sent will be ignored.
            before (ISO 8601 date and time): Only return pages where the page property value is before the provided date. Note that the comparison is done against the date. Any time information sent will be ignored.
            after (ISO 8601 date and time): Only return pages where the page property value is after the provided date. Note that the comparison is done against the date. Any time information sent will be ignored.
            on_or_before (ISO 8601 date and time): Only return pages where the page property value is on or before the provided date. Note that the comparison is done against the date. Any time information sent will be ignored.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
            on_or_after (ISO 8601 date and time): Only return pages where the page property value is on or after the provided date. Note that the comparison is done against the date. Any time information sent will be ignored.
            past_week (Dict): Only return pages where the page property value is within the past week.
            past_month (Dict): Only return pages where the page property value is within the past month.
            past_year (Dict): Only return pages where the page property value is within the past year.
            next_week (Dict): Only return pages where the page property value is within the next week.
            next_month (Dict): Only return pages where the page property value is within the next month.
            next_year (Dict): Only return pages where the page property value is within the next year.
    """

    property: str
    equals: str = None
    before: str = None
    after: str = None
    on_or_before: str = None
    is_empty: bool = None
    is_not_empty: bool = None
    on_or_after: str = None
    past_week: Dict = None
    past_month: Dict = None
    past_year: Dict = None
    next_week: Dict = None
    next_month: Dict = None
    next_year: Dict = None


@dataclass
class PeopleFilterCondition:
    """
        A people filter condition applies to database properties of types "created_by", and "last_edited_by"

            property (str): Property name
            contains (str): Only return pages where the page property value contains the provided value.
            does_not_contain (str): Only return pages where the page property value does not contain the provided value.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    contains: str = None
    does_not_contain: str = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class FileFiterCondition:
    """
        A file filter condition applies to database properties of type "files".

            property (str): Property name
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class RelationFilterCondition:
    """
        A relation filter condition applies to database properties of type "relation"

            property (str): Property name
            contains (str): Only return pages where the page property value contains the provided value.
            does_not_contain (str): Only return pages where the page property value does not contain the provided value.
            is_empty (bool (only true)): Only return pages where the page property value is empty.
            is_not_empty (bool (only true)): Only return pages where the page property value is present.
    """

    property: str
    contains: str = None
    does_not_contain: str = None
    is_empty: bool = None
    is_not_empty: bool = None


@dataclass
class FormulaFilterCondition:
    """
        A formula filter condition applies to database properties of type "formula"

            property (str): Property name
            text (TextFilterCondition): Only return pages where the page property value contains the provided value.
            checkbox (CheckboxFilterCondition): Only return pages where the page property value contains the provided value.
            number (NumberFilterCondition): Only return pages where the page property value contains the provided value.
            date (DateFilterCondition): Only return pages where the page property value contains the provided value.
    """

    property: str
    text: TextFilterCondition = None
    checkbox: CheckboxFilterCondition = None
    number: NumberFilterCondition = None
    date: DateFilterCondition = None


Filters = List[
    Union[
        TextFilterCondition, NumberFilterCondition, CheckboxFilterCondition, SelectFilterCondition, MultiSelectFilterCondition,
        DateFilterCondition, PeopleFilterCondition, FileFiterCondition, RelationFilterCondition, FormulaFilterCondition
    ]
]


@nested_dataclass
class CompoundFilter:
    or_field: Union[List[Type['CompoundFilter']], Filters] = field(default_factory=list)
    and_field: Union[List[Type['CompoundFilter']], Filters] = field(default_factory=list)


@nested_dataclass
class QueryBody:
    filters: Union[CompoundFilter, Filters] = None
    sorts: List[Sort] = None
