import json

class PersonDOM:
    def __init__(self, id, name, age, city_id):
        self.id = id
        self.name = name
        self.age = age
        self.city_id = city_id

    def toJSON(self):
        data = dict()
        data["name"] = self.name
        data["age"] = self.age

        return json.dumps(data)