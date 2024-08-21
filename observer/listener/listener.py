from abc import ABCMeta, abstractmethod
from domain.incident import Incident
from domain.incident_type import IncidentType

class Listener:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_assigned_type(self) -> IncidentType:
        pass

    @abstractmethod
    def process(self, target: Incident):
        pass

