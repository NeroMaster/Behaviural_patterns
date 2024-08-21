from datetime import datetime

from place.impl.museum import Museum, Note
from place.impl.park import Park
from place.impl.restaurant import Restaurant
from process.visitor import Visitor
from process.impl.auditor import Auditor

def main():
    museum = Museum(
        12.21,
        32.54,
        [],
        [Note("Exhibition of antiquities", datetime.utcnow(), datetime.utcnow())]
    )

    park = Park(
        13.25,
        34.64,
        []
    )

    restaurant = Restaurant(
        11.12,
        29.30,
        [],
        ["Borsch", "Dumplings"]
    )

    museum.assign_point(park)
    museum.assign_point(restaurant)

    park.assign_point(museum)
    park.assign_point(restaurant)

    restaurant.assign_point(museum)
    restaurant.assign_point(park)

    visitor = Auditor()
    museum_review = visitor.visit_museum(museum)
    print(museum_review)

if __name__ == "__main__":
    main()