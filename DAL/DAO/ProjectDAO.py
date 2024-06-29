from DAL.DAO.DataAccessObject import DataAccessObject

class ProjectDAO:

    def __init__(self):
        self.dao = DataAccessObject()

    def add_project(self, project_dom):
        sql = f"INSERT INTO projects (uuid, name) VALUES ('{project_dom.uuid}', '{project_dom.name}');"
        self.dao.execute_raw(sql)

    def get_all_projects(self):
        sql = """
            SELECT 
                projects.id, 
                projects.uuid, 
                projects.name
            FROM 
                projects 
            """
        return self.dao.query(sql)
    
    def remove_project_by_uuid(self, uuid):
        sql = f"DELETE FROM projects WHERE uuid = '{uuid}';"
        self.dao.execute_raw(sql)