import sqlite3
import os
import pandas as pd
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
    
    def query(self, sql):
        # Connect to your database
        self.connect()
        
        # Execute the query and fetch the results
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        
        # Get the column names from the cursor description
        columns = [col[0] for col in self.cur.description]
        
        # Fetch all rows as a list of dictionaries
        results = []
        for row in rows:
            row_dict = {}
            for idx, col in enumerate(columns):
                row_dict[col] = row[idx]
            results.append(row_dict)
        
        # Close the self.cur and connection
        self.disconnect()
        if len(results) == 1:
            return results[0]
        return results
    
    def execute_raw(self, sql):
        # Connect to your database
        self.connect()
        # Execute the query and fetch the results
        self.cur.execute(sql)
        self.conn.commit()
        # Close the self.cur and connection
        self.disconnect()