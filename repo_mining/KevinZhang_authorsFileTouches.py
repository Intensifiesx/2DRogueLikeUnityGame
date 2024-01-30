import csv
import requests

token = ''
repo = 'scottyab/rootbeer'

def github_auth(url):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    return response.json()

def get_commit_data(repo, filepath):
    commits_url = f'https://api.github.com/repos/{repo}/commits?path={filepath}'
    commits_data = github_auth(commits_url)
    return [(commit['commit']['author']['name'], commit['commit']['author']['date']) for commit in commits_data]

authors_file_data = []

# Read the source files from file_rootbeer.csv
with open('data/file_rootbeer.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        filepath = row['Filename']
        authors_dates = get_commit_data(repo, filepath)
        for author, date in authors_dates:
            authors_file_data.append([filepath, author, date])

# Save the collected data to a new CSV file
output_file = 'authors_file_touches.csv'
with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Filename', 'Author', 'Date'])
    writer.writerows(authors_file_data)

print(f'Author and date data saved to {output_file}')
