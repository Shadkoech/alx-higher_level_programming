#!/usr/bin/python3

"""Python script that takes 2 arguments in order to solve this challenge
    *list 10 commits (from the most recent to oldest) of
    the repository “rails” by the user “rails”
    """

import sys
import requests

if __name__ == "__main__":

    repo_name = sys.argv[1]
    user = sys.argv[2]
    url = ('https://api.github.com/repos/{}/{}/commits'
           .format(repo_name, user))

    req = requests.get(url)
    if req.status_code == 200:
        commits = req.json()[0:10]

    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f'{sha}: {author_name}')
