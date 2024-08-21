from typing import List
from place.point_of_interest import PointOfInterest

class Note:
    _name: str
    _start: str
    _end: str

    def __init__(self, name: str, start: str, end: str) -> None:
        self._name = name
        self._start = start
        self._end = end

    def get_name(self):
        return self._name
    
    def get_start(self):
        return self._start
    
    def get_end(self):
        return self._end

class Museum(PointOfInterest):

    _timetable: List[Note]

    def __init__(self, longitude: float, latitude: float, nearest, timetable) -> None:
        super().__init__(longitude, latitude, nearest)
        self._timetable = timetable

    def get_timetable(self):
        return self._timetable
