### Task DAO FUNCTIONS 

from DAL.DAO.DataAccessObject import DataAccessObject

class TaskDAO:

    def __init__(self):
        self.dao = DataAccessObject()

    def get_task_by_uuid(self, task_uuid):
        sql = f"SELECT tasks.id, tasks.uuid, tasks.name, tasks.description, tasks.due_date, tasks.priority, tasks.notes, tasks.project_id, projects.name AS project_name FROM tasks LEFT JOIN projects ON projects.id = tasks.project_id WHERE tasks.uuid = '{task_uuid}';"
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
                tasks.project_id,
                projects.name AS project_name 
            FROM 
                tasks 
            LEFT JOIN 
                projects 
            ON 
                tasks.project_id = projects.id;
            """
        return self.dao.query(sql)
    
    def get_all_tasks_in_project(self, project_id):
        sql = f"SELECT tasks.id, tasks.uuid, tasks.name, tasks.description, tasks.due_date, tasks.priority, tasks.notes, tasks.project_id, projects.name AS project_name FROM tasks LEFT JOIN projects ON projects.id = tasks.project_id WHERE tasks.project_id = '{project_id}';"
        return self.dao.query(sql)
    
    def add_task(self, task_dom):
        sql = f"INSERT INTO tasks (uuid, name, description, due_date, priority, notes, project_id) VALUES ('{task_dom.uuid}', '{task_dom.name}', '{task_dom.description}', '{task_dom.due_date}', '{task_dom.priority}', '{task_dom.notes}', '{task_dom.project.id}');"
        self.dao.execute_raw(sql)

    def remove_task_by_uuid(self, uuid):
        sql = f"DELETE FROM tasks WHERE uuid = '{uuid}';"
        self.dao.execute_raw(sql)