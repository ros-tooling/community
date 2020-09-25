import os
import sys

import requests

"""
This script sets up team access to all repositories in the organization according to
the level of permissions/responsibility set out in the governance model.

To use it, you must have a github access token with "admin:org" and "repo" permissions,
as this script reads repositories and sets permissions for teams, which uses org-level APIs

Workflow:

export GITHUB_TOKEN=your_token
python3 setup-permissions.py
"""


try:
    GITHUB_TOKEN = os.environ['GITHUB_TOKEN']
except KeyError:
    print('Environment variable GITHUB_TOKEN needs to be set')
    sys.exit(1)

ORGANIZATION = 'ros-tooling'
TEAM_PERMISSIONS = {
    'members': 'triage',
    # 'push' is equivalent to what the GUI shows as 'write'
    # reviewers need to have write access to be listed as CODEOWNERS
    # for automatic reviewer assignment
    'reviewers': 'push',
    'approvers': 'maintain',
    'owners': 'admin',
}


def check_request(request):
    """Check if a request had a good return code and raise if it doesn't."""
    if request.status_code == 200:
        return request.json()
    elif request.status_code == 204:
        return request
    else:
        raise RuntimeError('Request failed with code {}'.format(request.status_code))


def github_request(rest_method, endpoint, params=None):
    """Make an authenticated request to the GitHub API using the correct REST method."""
    headers = {'Authorization': 'token {}'.format(GITHUB_TOKEN)}
    print('Requesting {}({}) with params {}'.format(rest_method, endpoint, params))
    request = rest_method(
        'https://api.github.com/{}'.format(endpoint),
        headers=headers,
        json=params
    )
    return check_request(request)


def github_post(endpoint, params):
    return github_request(requests.post, endpoint, params)


def github_put(endpoint, params):
    return github_request(requests.put, endpoint, params)


def github_get(endpoint):
    return github_request(requests.get, endpoint)


def list_repos(org):
    """Return a list of the repositories under an organization."""
    return github_get('orgs/{}/repos'.format(org))


def set_team_permission(org, team, repo, permission):
    """For a given team in an organization, set its permissions for a repository."""
    return github_put(
        'orgs/{}/teams/{}/repos/{}/{}'.format(org, team, org, repo),
        {'permission': permission})


def setup_repo(org, repo):
    """For a repository, set up all the correct team permissions."""
    for team, permission in TEAM_PERMISSIONS.items():
        print(set_team_permission(org, team, repo, permission))


def main():
    repos = list_repos(ORGANIZATION)
    for repo_object in repos:
        repo_name = repo_object['name']
        print('Setting up {}'.format(repo_name))
        setup_repo(ORGANIZATION, repo_name)


if __name__ == '__main__':
    main()
