from copy import deepcopy
from typing import List
from domain.order import Order

class OrderHistory:
    _history: List[Order]

    def __init__(self) -> None:
        self._history = []

    def push(self, order: Order):
        self._history.append(order)

    def close(self):
        processed = deepcopy(self._history)
        self._history.clear()
        return processed
