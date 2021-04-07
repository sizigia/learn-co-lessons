import re
import os
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv('GITHUB_TOKEN')
username = os.getenv('USERNAME')

resp = requests.get(f'https://api.github.com/users/{username}/repos?per_page=150',
                    headers={'Authorization': auth_token})

repos = [repo for repo in resp.json() if repo['name'].endswith('000')]

git_urls = [repo['git_url'] for repo in repos]


def clone_repo(repo):
    folder = re.search(
        f"(?<=git://github\.com/{username}/).+(?=-000\.git)", repo).group()
    subprocess.Popen(
        ['git', 'clone', repo, folder])


[clone_repo(repo['git_url']) for repo in repos]
