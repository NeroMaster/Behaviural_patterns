from abc import ABCMeta, abstractclassmethod, abstractmethod
from entity.request import Request


class Support:
    __metaclass__ = ABCMeta
    _next = None

    @abstractmethod
    def _get_assigned_type(self):
        pass

    @abstractmethod
    def _pass(self, request: Request):
        if self._next is not None:
            self._next.process(request)
        return False

    @abstractclassmethod
    def link(cls, first, *args):
        head = first
        for next_in_chain in args:
            head._next = next_in_chain
            head = next_in_chain
        return first
    
    @abstractmethod
    def process(self, request: Request):
        pass
