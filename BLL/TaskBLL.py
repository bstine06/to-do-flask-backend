from DAL.DAO.TaskDAO import TaskDAO
from DAL.DOM.TaskDOM import TaskDOM


class TaskBLL:

  def __init__(self):
     self.task_dao = TaskDAO()

  def get_task_by_uuid(self, uuid):
    task_dom = TaskDOM()
    result = self.task_dao.get_task_by_uuid(uuid)[0]
    task_dom.from_dictionary(result)
    return(task_dom)
  
  def get_all_tasks(self, filters={}):
    result = list()
    for task in self.task_dao.get_all_tasks():
      task_dom = TaskDOM()
      task_dom.from_dictionary(task)
      result.append(task_dom)
    return result
  
  def get_all_tasks_in_project(self, project_id):
    result = list()
    for task in self.task_dao.get_all_tasks_in_project(project_id):
      task_dom = TaskDOM()
      task_dom.from_dictionary(task)
      result.append(task_dom)
    return result
  
  def add_task(self, uuid, name, description, due_date, priority, notes, project_id):
    task_dom = TaskDOM()
    task_dom.uuid = uuid
    task_dom.name = name
    task_dom.description = description
    task_dom.due_date = due_date
    task_dom.priority = priority
    task_dom.notes = notes
    task_dom.project.id = project_id
    self.task_dao.add_task(task_dom)

  def remove_task_by_uuid(self, uuid):
    self.task_dao.remove_task_by_uuid(uuid)
