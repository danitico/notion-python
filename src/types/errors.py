from dataclasses import dataclass


@dataclass
class NotionError:
    code: str
    message: str