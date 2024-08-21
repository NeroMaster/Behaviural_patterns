from typing import List, Dict

from domain.incident_type import IncidentType
from domain.incident import Incident
from listener.listener import Listener

class IncidentManager:
    _listeners: Dict[str, List[Listener]]

    def __init__(self) -> None:
        self._listeners = {
            IncidentType.SERVER_IS_DEAD.value: [],
            IncidentType.SERVER_TIMEOUT.value: [],
        }

    def subscribe(self, listener: Listener):
        self._listeners.get(listener.get_assigned_type().value).append(listener)

    def ubsubscribe(self, listener: Listener):
        self._listeners.get(listener.get_assigned_type().value).remove(listener)

    def notify(self, incident: Incident):
        for subscriber in self._listeners.get(incident.get_type().value):
            subscriber.process(incident)