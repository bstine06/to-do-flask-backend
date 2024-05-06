import os
import re
import sys
import glob
import pandas as pd
import numpy as np
import json
from flask import Flask, render_template, Blueprint, request, send_from_directory, send_file, flash, Blueprint, g, session, app, current_app, jsonify
from flask_wtf import Form
from BLL.PersonBLL import PersonBLL
from bs4 import BeautifulSoup as bs
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

@webapp.route("/")
def home():
  js_source, css_source = get_js__and_css_source()
  return  render_template("index.html.j2",
              js_source=js_source,
              css_source=css_source
          )

@webapp.route("/info")
def info():
  js_source, css_source = get_js__and_css_source()
  return  render_template("info.html.j2",
              js_source=js_source,
              css_source=css_source
          )

@webapp.route("/data", methods=["POST"])
def data():
  data = dict()
  data["name"] = "Brett"
  data["age"] = "27"
  data["country"] = "USA"
  return  json.dumps(data)  

@webapp.route("/get-person", methods=["POST"])
def get_person_by_id():
  person_bll = PersonBLL()
  data = request.json 
  id = data.get('id')
  result = person_bll.getPersonById(id)
  return jsonify(result.toDictionary()).json

@webapp.route("/get-people", methods=['POST'])
def get_people():
  person_bll = PersonBLL()
  result = person_bll.getAllPeople()  
  return jsonify([jsonify(item.toDictionary()).json for item in result])

@webapp.route("/add-person", methods=['POST'])
def add_person():
  person_bll = PersonBLL()
  data = request.json 
  age = data.get('age')
  name = data.get('name')
  person_bll.add_person(age, name)
  return jsonify({"result":True}).json

@webapp.route("/remove-person", methods=['POST'])
def remove_person():
  person_bll = PersonBLL()
  data = request.json 
  id = data.get('id')
  person_bll.remove_person(id)
  return jsonify({"result":True}).json

