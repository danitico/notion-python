from dataclasses import dataclass, field
from typing import List, Literal, Type

from .rich_text import RichText


@dataclass
class Block:
    id = str
    type: Literal[
        'paragraph', 'heading_1', 'heading_2', 'heading_3',
        'bulleted_list_item', 'numbered_list_item', 'to_do',
        'toggle', 'child_page', 'unsupported'
    ]
    created_time: str
    last_edited_time: str
    has_children: bool
    text: List[RichText] = field(default_factory=list)
    children: List[Type['Block']] = field(default_factory=list)
    title: str = None
    checked: bool = False
    object: str = 'block'

    def is_paragraph_block(self) -> bool:
        return self.type == 'paragraph'

    def is_heading_1_block(self) -> bool:
        return self.type == 'heading_1'

    def is_heading_2_block(self) -> bool:
        return self.type == 'heading_2'

    def is_heading_3_block(self) -> bool:
        return self.type == 'heading_3'

    def is_bulleted_list_item_block(self) -> bool:
        return self.type == 'bulleted_list_item'

    def is_numbered_list_item_block(self) -> bool:
        return self.type == 'numbered_list_item'

    def is_to_do_block(self) -> bool:
        return self.type == 'to_do'

    def is_toggle_block(self) -> bool:
        return self.type == 'toggle'

    def is_child_page_block(self) -> bool:
        return self.type == 'child_page'

    def is_unsupported_block(self) -> bool:
        return self.type == 'unsupported'
