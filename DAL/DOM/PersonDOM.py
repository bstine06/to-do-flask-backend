import json
from DAL.DOM.CityDOM import CityDOM

class PersonDOM:
    def __init__(self, id, name, age, city_id, city_name=None):
        if city_name is None:
            self.city_id = city_id
            pass
        else:
            self.city = CityDOM(city_id, city_name)
        self.id = id
        self.name = name
        self.age = age

    def toDictionary(self):
        data = dict()
        data["name"] = self.name
        data["age"] = self.age
        if hasattr(self, "city"):
            data["city_name"] = self.city.name
        return data

    def toJSON(self):
        return json.dumps(self.toDictionary())