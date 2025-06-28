class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")
        if name is not None and age is not None:
            person = Person(name, age)
            person_list.append(person)

    for person_data, person in zip(people, person_list):
        if "wife" in person_data:
            if person_data["wife"] is None:
                continue
            if person_data["wife"] in Person.people:
                person.wife = Person.people[person_data["wife"]]
        if "husband" in person_data:
            if person_data["husband"] is None:
                continue
            if person_data["husband"] in Person.people:
                person.husband = Person.people[person_data["husband"]]

    return person_list