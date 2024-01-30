import json
import requests
import csv
import os
import pandas as pd

lstTokens = 'fakeToken'
API_URL = 'https://api.github.com'

# GitHub repo
repo = 'scottyab/rootbeer'

# Headers for authentication
headers = {
    'Authorization': f'token {lstTokens}',
    'Accept': 'application/vnd.github.v3+json',
}

# List of source file extensions
source_extensions = ['.java', '.kt', '.xml']  

def is_source_file(filename):
    # Check for source file extension
    return any(filename.endswith(ext) for ext in source_extensions)

def get_commits(repo):
    commits = []
    page = 1
    while True:
        # Construct the API URL for commits
        commits_url = f'{API_URL}/repos/{repo}/commits?page={page}&per_page=100'
        response = requests.get(commits_url, headers=headers)
        response.raise_for_status()  
        commit_data = response.json()
        if not commit_data:  # Break the loop if no more commits are returned
            break
        commits.extend(commit_data)
        page += 1
    return commits

# Get the list of commits for the repo
commits = get_commits(repo)

# List to hold commit details for source files
commit_details = []

# Loop over each commit to get detailed information
for commit in commits:
    sha = commit['sha']
    commit_url = f'{API_URL}/repos/{repo}/commits/{sha}'
    response = requests.get(commit_url, headers=headers)
    response.raise_for_status()
    commit_data = response.json()

    # Extract relevant data
    author_name = commit_data['commit']['author']['name']
    commit_date = commit_data['commit']['author']['date']

    for file in commit_data['files']:
        if is_source_file(file['filename']):
            # Ensure dictionary keys match the expected column names
            commit_details.append({
                'Filename': file['filename'],  # Match the expected column name
                'Author': author_name,        # Match the expected column name
                'Date': commit_date           # Match the expected column name
            })

# Convert to DataFrame
df_commits = pd.DataFrame(commit_details)

# Save to CSV
df_commits.to_csv('data/authorsFileTouches.csv', index=False)

print("Data saved to 'data/authorsFileTouches.csv'")
