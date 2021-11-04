from github import Github
import requests

# Token
g = Github("<insert token>")

# Gets list of my repos
for repo in g.get_user().get_repos(''):
    print(repo.name)

# Get clone URL of repo 'BLAH' / 'aprivateone'
repo = g.get_repo("Izardo/Random-Notebooks")
print(repo.clone_url)

# Download url of file in this repo
file_info = repo.get_contents("README.md")
url = file_info.download_url
#print(url)

# Request to get content of file
response = requests.get(url)
content = response.text
#print(content)

# Append new content
new_content = content + ' more stuff \n'
print(new_content)

# repo.update_file() function
git_response = repo.update_file(file_info.path, 'updated by prog', new_content, file_info.sha)
print(git_response)

