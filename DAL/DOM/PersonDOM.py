import json
from DAL.DOM.CityDOM import CityDOM

class PersonDOM:
    def __init__(self):
        self.city = CityDOM()
        self.id = None
        self.name = None
        self.age = None

    def toDictionary(self):
        data = dict()
        data["name"] = self.name
        data["age"] = self.age
        data["city_id"] = self.city.id
        data["city_name"] = self.city.name
        return data
    
    def from_dictionary(self, dict):
        if "city_name" in dict.keys():
            self.city.name = dict["city_name"]
        self.city.id = dict["city_id"]
        self.id = dict["id"]
        self.name = dict["name"]
        self.age = dict["age"]

    def toJSON(self):
        return json.dumps(self.toDictionary())