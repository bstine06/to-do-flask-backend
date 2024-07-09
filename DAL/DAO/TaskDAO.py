### Task DAO FUNCTIONS 

from DAL.DAO.DataAccessObject import DataAccessObject

class TaskDAO:

    def __init__(self):
        self.dao = DataAccessObject()

    def get_task_by_uuid(self, task_uuid):
        sql = f"SELECT tasks.id, tasks.uuid, tasks.name, tasks.description, tasks.due_date, tasks.priority, tasks.notes, tasks.project_uuid, projects.name AS project_name FROM tasks LEFT JOIN projects ON projects.id = tasks.project_id WHERE tasks.uuid = '{task_uuid}';"
        return self.dao.query(sql)
    
    def get_all_tasks(self):
        sql = """
            SELECT 
                tasks.id, 
                tasks.uuid, 
                tasks.name, 
                tasks.description, 
                tasks.due_date, 
                tasks.priority, 
                tasks.notes, 
                tasks.project_uuid,
                projects.name AS project_name 
            FROM 
                tasks 
            LEFT JOIN 
                projects 
            ON 
                tasks.project_uuid = projects.uuid;
            """
        return self.dao.query(sql)
    
    def get_all_tasks_in_project(self, project_uuid):
        sql = f"SELECT tasks.id, tasks.uuid, tasks.name, tasks.description, tasks.due_date, tasks.priority, tasks.notes, tasks.project_uuid, projects.name AS project_name FROM tasks LEFT JOIN projects ON projects.uuid = tasks.project_uuid WHERE tasks.project_uuid = '{project_uuid}';"
        return self.dao.query(sql)
    
    def add_task(self, task_dom):
        sql = f"INSERT INTO tasks (uuid, name, description, due_date, priority, notes, project_uuid) VALUES ('{task_dom.uuid}', '{task_dom.name}', '{task_dom.description}', '{task_dom.due_date}', '{task_dom.priority}', '{task_dom.notes}', '{task_dom.project.uuid}');"
        self.dao.execute_raw(sql)

    def remove_task_by_uuid(self, uuid):
        sql = f"DELETE FROM tasks WHERE uuid = '{uuid}';"
        self.dao.execute_raw(sql)