import sqlite3
import os
from DAL.DOM.PersonDOM import PersonDOM

this_files_dir = os.path.dirname(os.path.abspath(__file__))

class DataAccessObject:
    def __init__(self):
        self.db_file = f"{this_files_dir}/../../DATA/mydatabase.db"
        

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def get_person_by_id(self, person_id):
        self.connect()
        self.cur.execute("SELECT * FROM People WHERE id = ?", (person_id,))
        person_data = self.cur.fetchone()
        self.disconnect()

        if person_data:
            return PersonDOM(*person_data)
        else:
            return None

    def get_all_people(self):
        self.connect()
        self.cur.execute("SELECT * FROM People")
        people_data = self.cur.fetchall()
        self.disconnect()

        people = []
        for person_data in people_data:
            people.append(PersonDOM(*person_data))
        return people