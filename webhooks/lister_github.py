from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return "Welcome Gagan"

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        json_reponse = json.dumps(request.json)
        print(json_reponse)
        return json_reponse

if __name__ == '__main__':
    app.run(debug=True)