import sys
import json
import yaml
from flask import Flask
from github import Github
from flask import jsonify


app = Flask(__name__)
url = sys.argv[1].split("/")

for i in range(len(url)):
    if "github" in url[i]:
        user = url[i+1]
        repo = url[i+2]
        break