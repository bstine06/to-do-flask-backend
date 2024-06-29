import json
class ProjectDOM:

  def __init__(self):
    self.id = None
    self.uuid = None
    self.name = None

  def toDictionary(self):
    data = dict()
    data["uuid"] = self.uuid
    data["name"] = self.name
    return data
  
  def from_dictionary(self, dict):
    self.id = dict["id"]
    self.uuid = dict["uuid"]
    self.name = dict["name"]

  def toJSON(self):
    return json.dumps(self.toDictionary())