from place.point_of_interest import PointOfInterest

class Park(PointOfInterest):
    def __init__(self, longitude: float, latitude: float, nearest) -> None:
        super().__init__(longitude, latitude, nearest)

