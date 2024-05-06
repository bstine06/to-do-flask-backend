### PERSON DAO FUNCTIONS 

from DAL.DAO.DataAccessObject import DataAccessObject

class PersonDAO:

    def __init__(self):
        self.dao = DataAccessObject()

    def get_person_by_id(self, person_id):
        sql = f"SELECT people.id, people.name, people.age, people.city_id, cities.name AS city_name FROM people LEFT JOIN cities ON cities.id = people.city_id WHERE people.id = {person_id};"
        return self.dao.query(sql)
    
    def get_all_people(self):
        sql = "SELECT people.id, people.name, people.age, people.city_id, cities.name AS city_name FROM people LEFT JOIN cities ON cities.id = people.city_id;"
        return self.dao.query(sql)
    
    def add_person(self, person_dom):
        sql = f"INSERT INTO people (name, age) VALUES ('{person_dom.name}', '{person_dom.age}');"
        self.dao.execute_raw(sql)

    def remove_person(self, id):
        sql = f"DELETE FROM people WHERE id = '{id}';"
        self.dao.execute_raw(sql)