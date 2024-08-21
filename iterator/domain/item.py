from enum import Enum

class ItemType(Enum):
    ARMOR = "ARMOR"
    WEAPON = "WEAPON"
    CHEMISTRY = "CHEMISTRY"
    JEWELRY = "JEWERLY"

class Item:
    _name: str
    _type: ItemType
    
    def __init__(self, name: str, item_type: ItemType) -> None:
        self._name = name
        self._type = item_type

    def get_name(self):
        return self._name
    
    def get_type(self):
        return self._type
    