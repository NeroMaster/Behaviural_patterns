from typing import List
from place.point_of_interest import PointOfInterest

class Restaurant(PointOfInterest):
    _menu: List[str]

    def __init__(self, longitude: float, latitude: float, nearest, menu) -> None:
        super().__init__(longitude, latitude, nearest)
        self._menu = menu

    def get_menu(self):
        return self._menu

