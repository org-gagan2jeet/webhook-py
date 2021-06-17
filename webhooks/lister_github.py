import requests
from flask import json
from flask import request
from flask import Flask, render_template
import config
from gitapi import github

app = Flask(__name__)
app.register_blueprint(github, url_prefix="/api")
@app.route('/')
def api_root():
    return "This is the FLASK Web API"

if __name__ == '__main__':
    app.run(debug=True)