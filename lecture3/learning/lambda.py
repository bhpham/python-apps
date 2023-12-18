people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Revenclaw"},
    {"name": "Draco", "house": "Slytherin"}

]

people.sort(key=lambda person: person["house"])
print(people)