from typing import List
from domain.order import Order

class DeliveryOrder(Order):
    def __init__(self, name: str, description: List[str]) -> None:
        super().__init__(name, description)

    def process(self):
        print(f"Delivery Order from {self.get_name()} was processed!")
        return True