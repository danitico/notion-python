from dataclasses import dataclass


@dataclass
class DateProperty:
    start: str
    end: str = ''

    def is_date_range(self):
        return not self.end


@dataclass
class QueryParams:
    start_cursor: str
    page_size: int

    def __post_init__(self):
        if self.page_size >= 100:
            self.page_size = 100