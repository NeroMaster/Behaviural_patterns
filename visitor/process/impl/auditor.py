from place.impl.museum import Museum
from place.impl.park import Park
from place.impl.restaurant import Restaurant
from process.visitor import Visitor

class Auditor(Visitor):
    def visit_museum(self, museum: Museum):
        print(f"I visited a museum arranged by latitude and longitude: {museum.get_latitude()}:{museum.get_longitude()}. \
              And get timetable with {len(museum.get_timetable())} notes!")
        
    def visit_park(self, park: Park):
        print(f"I visited a park arranged by latitude and longitude: {park.get_latitude()}:{park.get_longitude()}. And get nice photos!")

    def visit_restaurant(self, restraunt: Restaurant):
       print(f"I visited a museum arranged by latitude and longitude: {restraunt.get_latitude()}:{restraunt.get_longitude()}. \
             And get menu with {len(restraunt.get_nearest())} entities!")
