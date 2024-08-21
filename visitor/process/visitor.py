from abc import ABCMeta, abstractmethod

from place.impl.museum import Museum
from place.impl.park import Park
from place.impl.restaurant import Restaurant

class Visitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visit_museum(self):
        pass

    @abstractmethod
    def visit_park(self):
        pass

    @abstractmethod
    def visit_restaurant(self):
        pass
