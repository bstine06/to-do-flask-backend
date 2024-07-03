import setproctitle
from gevent.pywsgi import WSGIServer
from API.api import webapp # where the magic happens
from flask import Flask, redirect, url_for, render_template, Blueprint, session, app, flash, jsonify
import os
from flask_cors import CORS

debug = True

hostname = 'Brett'

ALLOWED_ORIGIN = "http://127.0.0.1:5500" # the only external domain allowed to request this server

app = Flask(__name__)
app.register_blueprint(webapp)
CORS(app, origins=ALLOWED_ORIGIN)  # Allow only this origin for all routes

# app.config['UPLOAD_FOLDER'] = '/static/'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def main():

	#For developers, use this
	app.run(debug=debug, host='127.0.0.1', port=5006)

	# For server, use this
	# app.config['SERVER_NAME'] = 'facemorph.com:5000'	# only for running on server
	# app.run(debug=debug)

	# Magically calling route "/" in api_routes.py (O.o)

main()