from dataclasses import dataclass


@dataclass
class Date:
    start: str
    end: str = ''

    def is_date_range(self):
        return not self.end