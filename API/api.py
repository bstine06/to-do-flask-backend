import os
import re
import sys
import glob
import pandas as pd
import numpy as np
import json
from flask import Flask, render_template, Blueprint, request, send_from_directory, send_file, flash, Blueprint, g, session, app, current_app, jsonify
from flask_wtf import Form
from BLL.TaskBLL import TaskBLL
from BLL.ProjectBLL import ProjectBLL
# from bs4 import BeautifulSoup as bs
from werkzeug.utils import secure_filename
from pathlib import Path


this_files_dir = os.path.dirname(os.path.abspath(__file__))

webapp = Blueprint("webapp",
          __name__,
          template_folder=f"{this_files_dir}/../DEPENDENCIES/HTML",
          static_folder="DEPENDENCIES/JS",
          static_url_path="/static"
          )

def get_js__and_css_source():

  # Add js files here as you create them

  js_dir = f"{this_files_dir}/../DEPENDENCIES/JS"
  css_dir = f"{this_files_dir}/../DEPENDENCIES/CSS"

  js_source = ""
  for js_filename in glob.glob(f"{js_dir}/*.js"):
    with open(js_filename, "r") as f:
      js_source += f.read()

  css_source = ""
  for css_filename in glob.glob(f"{css_dir}/*.css"):
    with open(css_filename, "r") as f:
      css_source += f.read()

  return js_source, css_source

@webapp.route('/health-check', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200

@webapp.route("/get-task-by-uuid", methods=["POST"])
def get_task_by_uuid():
  task_bll = TaskBLL()
  data = request.json 
  uuid = data.get('uuid')
  result = task_bll.get_task_by_uuid(uuid)
  return jsonify(result.toDictionary()).json

@webapp.route("/get-all-tasks", methods=['GET'])
def get_all_tasks():
  task_bll = TaskBLL()
  result = task_bll.get_all_tasks()  
  return jsonify([jsonify(item.toDictionary()).json for item in result])

@webapp.route("/get-all-tasks-in-project", methods=['POST'])
def get_all_tasks_in_project():
  task_bll = TaskBLL()
  data = request.json
  project_uuid = data.get('project_uuid')
  result = task_bll.get_all_tasks_in_project(project_uuid)
  return jsonify([jsonify(item.toDictionary()).json for item in result])

@webapp.route("/add-task", methods=['POST'])
def add_task():
  task_bll = TaskBLL()
  data = request.json 
  uuid = data.get('uuid')
  name = data.get('name')
  description = data.get('description')
  due_date = data.get('due_date')
  priority = data.get('priority')
  notes = data.get('notes')
  project_id = data.get('project_id')
  task_bll.add_task(uuid, name, description, due_date, priority, notes, project_id)
  return jsonify({"result":True}).json

@webapp.route("/remove-task-by-uuid", methods=['POST'])
def remove_task_by_uuid():
  task_bll = TaskBLL()
  data = request.json 
  uuid = data.get('uuid')
  task_bll.remove_task_by_uuid(uuid)
  return jsonify({"result":True}).json

@webapp.route("/add-project", methods=['POST'])
def add_project():
  project_bll = ProjectBLL()
  data = request.json
  uuid = data.get('uuid')
  name = data.get('name')
  project_bll.add_project(uuid, name)
  return jsonify({"result":True}).json

@webapp.route("/get-all-projects", methods=['GET'])
def get_all_projects():
  project_bll = ProjectBLL()
  result = project_bll.get_all_projects()  
  return jsonify([jsonify(item.toDictionary()).json for item in result])

@webapp.route("/remove-project-by-uuid", methods=['POST'])
def remove_project_by_uuid():
  project_bll = ProjectBLL()
  data = request.json
  uuid = data.get('uuid')
  project_bll.remove_project_by_uuid(uuid)
  return jsonify({"result":True}).json