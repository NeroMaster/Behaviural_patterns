from typing import List
from abc import ABCMeta, abstractmethod

class Order:
    __metaclass__ = ABCMeta
    
    _name: str
    _description: List[str]

    def __init__(self, name: str, description: List[str]) -> None:
        self._name = name
        self._description = description

    @abstractmethod
    def process(self):
        pass

    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description

