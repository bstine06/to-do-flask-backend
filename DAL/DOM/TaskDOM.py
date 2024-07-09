import json
from DAL.DOM.ProjectDOM import ProjectDOM

class TaskDOM:
    def __init__(self):
        self.project = ProjectDOM()
        self.id = None
        self.uuid = None
        self.name = None
        self.description = None
        self.due_date = None
        self.priority = None
        self.notes = None

    def toDictionary(self):
        data = dict()
        data["uuid"] = self.uuid
        data["name"] = self.name
        data["description"] = self.description
        data["due_date"] = self.due_date
        data["priority"] = self.priority
        data["project_uuid"] = self.project.uuid
        data["project_name"] = self.project.name
        data["notes"] = self.notes
        return data
    
    def from_dictionary(self, dict):
        self.project.name = dict["project_name"]
        self.project.uuid = dict["project_uuid"]
        self.id = dict["id"]
        self.uuid = dict["uuid"]
        self.name = dict["name"]
        self.description = dict["description"]
        self.due_date = dict["due_date"]
        self.priority = dict["priority"]
        self.notes = dict["notes"]

    def toJSON(self):
        return json.dumps(self.toDictionary())