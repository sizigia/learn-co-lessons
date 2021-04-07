import os
from transfer import TransferRepos
from dotenv import load_dotenv

load_dotenv()
auth_token = os.getenv('GITHUB_TOKEN')
username = os.getenv('USERNAME')
transfer_user = os.getenv('TRANSFER_USER')

client = TransferRepos(auth_token, username, transfer_user)

for repo in client.get_repos():
    if repo.endswith('000'):
        client.transfer_repo(repo)
