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


def get_response(config_file):
    return git.get_file_contents(config_file).content.decode(git.get_contents(config_file).encoding)

    if extn=="json":
                return jsonify(yaml.safe_load(git.get_file_contents(filename+".yml").content.decode(git.get_contents(filename+".yml").encoding)))
            elif extn=="yml":
                response = yaml.safe_dump(json.loads(git.get_file_contents(filename+".json").content.decode(git.get_contents(filename+".json").encoding)))
                response = response[1:len(response)-2]
                return response


@app.route("/v1/<config_file>")
def controller(config_file):
    #check if connection to github errored out
    if isinstance(git, basestring):
        return git
    else:
        return get_required_response(config_file)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')