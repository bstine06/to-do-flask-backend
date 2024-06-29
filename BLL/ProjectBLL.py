from DAL.DAO.ProjectDAO import ProjectDAO
from DAL.DOM.ProjectDOM import ProjectDOM

class ProjectBLL:

  def __init__(self):
    self.project_dao = ProjectDAO()
  
  def add_project(self, uuid, name):
    project_dom = ProjectDOM()
    project_dom.uuid = uuid
    project_dom.name = name
    self.project_dao.add_project(project_dom)

  def get_all_projects(self):
    result = list()
    for project in self.project_dao.get_all_projects():
      project_dom = ProjectDOM()
      project_dom.from_dictionary(project)
      result.append(project_dom)
    return result
  
  def remove_project_by_uuid(self, uuid):
    self.project_dao.remove_project_by_uuid(uuid)
