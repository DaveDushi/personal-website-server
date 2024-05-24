import os
import requests
import json
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from flask import Flask, send_from_directory, request, jsonify, redirect, render_template
from dotenv import load_dotenv
import logging

load_dotenv()

ROOT_FOLDER = "Projects/Personal Website/frontend/personal-website/build"
app = Flask(__name__, static_folder=ROOT_FOLDER, static_url_path='/')
# app.debug = False

# app = Flask(__name__)

CORS(app)  # allows cors for our frontend

logging.basicConfig(level=logging.DEBUG)

#Configure Database
app.config['DATABASE_URI'] = os.getenv('DATABASE_URI')


URI = app.config['DATABASE_URI']
client = MongoClient(URI,
                     tls=True,
                     tlsAllowInvalidCertificates=True)

database = client.get_database('personal_website')


@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/projects')
def get_projects():
    projects = database.get_collection('projects')
    data = list(projects.find({},{'_id': False}))
    return jsonify(data)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    return jsonify({"message": 'Message Sent'})


if __name__ == '__main__':
    app.run(debug=True)
