from typing import List

from process.kitchen import Kitchen
from domain.order import Order
from domain.impl.hall_order import HallOrder
from domain.impl.delivery_order import DeliveryOrder

def main():
    kitchen = Kitchen()
    hall: Order = HallOrder(
        name="Hall Enjoyer",
        description=["Dishes", "For", "Hall"]
    )
    kitchen.process(hall)

    delivery: Order = DeliveryOrder(
        name="Delivery Chad",
        description=["Dishes", "For", "Delivery"]
    )
    kitchen.process(delivery)

    processed: List[Order] = kitchen.close()
    for pr in processed:
        print(f"An order for {pr.get_name()} was completed today!")

if __name__ == "__main__":
    main()