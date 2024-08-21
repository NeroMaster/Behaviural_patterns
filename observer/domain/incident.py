from domain.incident_type import IncidentType

class Incident:
    _type: IncidentType
    _description: str

    def __init__(self, incident_type: IncidentType, description: str) -> None:
        self._type = incident_type
        self._description = description

    def get_type(self):
        return self._type
    
    def get_description(self):
        return self._description
    
