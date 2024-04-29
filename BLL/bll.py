import os
import sys
from DAL.DAO.DataAccessObject import DataAccessObject

class BusinessLogicLayer:

  def __init__(self):
    self.data_access_object = DataAccessObject()

  def getPerson(self, id):
    person = self.data_access_object.get_person_by_id(id)
    return person.toJSON()
    