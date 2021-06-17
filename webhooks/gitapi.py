import requests
from flask import Flask, redirect, url_for
from flask import request
from flask import Blueprint
import config
from flask import json

github = Blueprint("github", __name__)

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token " + config.UserPersonalAccessToken
}

repoOwner = ''
repoName = ''


@github.route('/repos')
def get_repos():
    githubRepos = requests.get(config.GITHUB_API + 'orgs/org-gagan2jeet/repos')
    if githubRepos.content:
        print(githubRepos.content)
        return githubRepos.content
    else:
        return githubRepos.content


@github.route('/addrepo', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        json_reponse = request.json
        if(json_reponse["action"] == "created"):
            repoName = json_reponse["repository"]["name"]
            repoOwner = json_reponse["repository"]["owner"]["login"]
            payload = '{"required_status_checks":{"strict":true,"contexts":["contexts"]},"enforce_admins":true,"required_pull_request_reviews":{"dismissal_restrictions":{"users":["users"],"teams":["teams"]},"dismiss_stale_reviews":true,"require_code_owner_reviews":true},"restrictions":{"users":["users"],"teams":["teams"],"apps":["apps"]}}'
            url = config.GITHUB_API + "repos/" + \
                repoOwner + "/" + repoName + "/branches/main/protection"
            postGitHubPernissions = requests.put(
                url, data=payload, headers=headers)
            issueBody = "@gaganyahoo the settings applied-" + str(postGitHubPernissions.content)
            
            issueData = {}
            issueData['title'] = 'The repository has been updated'
            issueData['body'] = issueBody
            
            url = config.GITHUB_API + "repos/" + repoOwner + "/" + repoName + "/issues"
            print(url)
            postGitHubMention = requests.post(
                url, data=json.dumps(issueData), headers=headers)
            print(postGitHubMention.content)
            return postGitHubMention.content

        else:
            return json_reponse
