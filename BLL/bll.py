import os
import sys
import json
from DAL.DAO.DataAccessObject import DataAccessObject
from DAL.DOM.PersonDOM import PersonDOM

class BusinessLogicLayer:

  def __init__(self):
    self.data_access_object = DataAccessObject()

  def getPersonById(self, id):
    person = self.data_access_object.get_person_by_id(id)
    return person.toJSON()
  
  def getAllPeople(self):
    results = list()
    all_people = self.data_access_object.get_all_people()
    for person in all_people:
        person = PersonDOM(*person)
        results.append(person.toDictionary())
    return json.dumps(results)
  
  def getAllPeopleWithCities(self):
    results = list()
    all_people_with_cities = self.data_access_object.get_all_people_with_cities()
    for person in all_people_with_cities:
      person = PersonDOM(*person)
      results.append(person.toDictionaryWithCities())
    return json.dumps(results)
