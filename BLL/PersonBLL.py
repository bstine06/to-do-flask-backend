from DAL.DAO.PersonDAO import PersonDAO
from DAL.DOM.PersonDOM import PersonDOM


class PersonBLL:

  def __init__(self):
     self.person_dao = PersonDAO()

  def getPersonById(self, id):
    person_dom = PersonDOM()
    result = self.person_dao.get_person_by_id(id)
    person_dom.from_dictionary(result)
    return(person_dom)
  
  def getAllPeople(self, filters={}):
    result = list()
    for person in self.person_dao.get_all_people():
      person_dom = PersonDOM()
      person_dom.from_dictionary(person)
      result.append(person_dom)
    return result
  
  def add_person(self, age, name):
    person_dom = PersonDOM()
    person_dom.age = age
    person_dom.name = name
    self.person_dao.add_person(person_dom)

  def remove_person(self, id):
    self.person_dao.remove_person(id)
