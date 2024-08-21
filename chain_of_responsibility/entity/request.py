from chain.support_type import SupportType
from datetime import datetime


class Request:
    _name: str
    _type: SupportType
    _created_on: datetime
    _description: str

    def __init__(self, name: str, support_type: SupportType, description: str) -> None:
        self._name = name
        self._type = support_type
        self._description = description
        self._created_on = datetime.utcnow()

    def get_name(self):
        return self._name

    def get_type(self):
        return self._type
    
    def get_created_on(self):
        return self._created_on
    
    def get_description(self):
        return self._description