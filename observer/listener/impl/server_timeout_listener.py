from listener.listener import Listener
from domain.incident import Incident
from domain.incident_type import IncidentType

class ServerTimeoutListener(Listener):
    def get_assigned_type(self) -> IncidentType:
        return IncidentType.SERVER_TIMEOUT
    
    def process(self, target: Incident):
        print(f"{self} Fetch SERVER_TIMEOUT incident with description: {target.get_description()}")
        return super().process(target)