from domain.chest import Chest
from domain.chest import ChestIterator
from domain.item import Item, ItemType

BLOCK_DELIMITER = "\n"

def revision(iterator):
    for it in iterator:
        print(f"{it.get_type()} {it.get_name()} presented in chest!")
        
def main():
    adventurer_chest = Chest([
        Item("Ring of Protection", ItemType.JEWELRY),
        Item("Fire Sword", ItemType.WEAPON),
        Item("Elven Cloak", ItemType.ARMOR),
        Item("Ring of Doom", ItemType.JEWELRY),
        Item("Amulet of Health", ItemType.JEWELRY),
        Item("Acid Bomb", ItemType.CHEMISTRY),
        Item("Potion of health", ItemType.CHEMISTRY),
        Item("Potion of mana", ItemType.CHEMISTRY),
        Item("Great Axe", ItemType.WEAPON),
        Item("Winged Helmet", ItemType.ARMOR),
    ])
    jewerly_iterator = iter(list(filter(lambda x: x.get_type() is ItemType.JEWELRY, adventurer_chest._content)))
    revision(jewerly_iterator)
    print(BLOCK_DELIMITER)

    armor_iterator = iter(list(filter(lambda x: x.get_type() is ItemType.ARMOR, adventurer_chest._content)))
    revision(armor_iterator)
    print(BLOCK_DELIMITER)

    weapon_iterator = iter(list(filter(lambda x: x.get_type() is ItemType.WEAPON, adventurer_chest._content)))
    revision(weapon_iterator)
    print(BLOCK_DELIMITER)

    chemistry_iterator = iter(list(filter(lambda x: x.get_type() is ItemType.CHEMISTRY, adventurer_chest._content)))
    revision(chemistry_iterator)
    print(BLOCK_DELIMITER)

if __name__ == "__main__":
    main()