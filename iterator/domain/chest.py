from typing import List

from domain.item import Item, ItemType

class ChestIterator:
    _content: List[Item]
    _current: int

    def __init__(self, content: List[Item]) -> None:
        self._current = 0
        self._content = content

    def has_next(self):
        return True if self._current < len(self._content) else False

    def __next__(self):
        self._current += 1
        return self._content[self._current - 1]

class Chest:

    _content: List[Item]

    def __init__(self, items: List[Item]) -> None:
        self._content = items





    