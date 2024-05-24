import os
from pymongo import MongoClient
from dotenv import load_dotenv
import json

load_dotenv()

URI = os.getenv('DATABASE_URI')
client = MongoClient(URI,
                     tls=True,
                     tlsAllowInvalidCertificates=True)

database = client.get_database('personal_website')

project_name = input("Enter the project name: ")
project_description = input("Enter the project description: ")
project_url = input("Enter the project link: ")
project_video = input("Enter project video link: ")

project = {
    "name": project_name,
    "description": project_description,
    "link": project_url,
    "videoPath": project_video
}

json_project = json.dumps(project)


projects = database.get_collection('projects')
projects.insert_one(project)

print("Added Project")


