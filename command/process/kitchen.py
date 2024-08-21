from process.order_history import OrderHistory
from domain.order import Order

class Kitchen:
    _history: OrderHistory

    def __init__(self) -> None:
        self._history = OrderHistory()

    def process(self, order: Order):
        is_processed = order.process()
        if is_processed:
            self._history.push(order)

    def close(self):
        return self._history.close()
