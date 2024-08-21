from abc import ABCMeta, abstractmethod

class PointOfInterest:
    __metaclass__ = ABCMeta

    _longitude: float
    _latitude: float

    _nearest = []

    def __init__(self, longitude: float, latitude: float, nearest) -> None:
        self._longitude = longitude
        self._latitude = latitude
        self._nearest = nearest

    def assign_point(self, point):
        self._nearest.append(point)

    def remove_point(self, point):
        self._nearest.remove(point)

    def get_longitude(self):
        return self._longitude
    
    def get_latitude(self):
        return self._latitude
    
    def get_nearest(self):
        return self._nearest

