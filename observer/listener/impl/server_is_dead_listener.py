from listener.listener import Listener
from domain.incident import Incident
from domain.incident_type import IncidentType

class ServerIsDeadListener(Listener):
    def get_assigned_type(self) -> IncidentType:
        return IncidentType.SERVER_IS_DEAD
    
    def process(self, target: Incident):
        print(f"{self} Fetch SERVER_IS_DEAD incident with description: {target.get_description()}")
        return super().process(target)