import json
import requests
import csv
import os

if not os.path.exists("data"):
    os.makedirs("data")

# GitHub Authentication function
def github_auth(url, lsttoken, ct):
    jsonData = None
    try:
        ct = ct % len(lstTokens)
        headers = {'Authorization': 'Bearer {}'.format(lstTokens[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        print(e)
    return jsonData, ct

# Function to count files
def count_files(dict_files, lst_tokens, repo):
    ipage = 1 
    ct = 0 

    while True:
        spage = str(ipage)
        commits_url = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
        json_commits, ct = github_auth(commits_url, lst_tokens, ct)

        if len(json_commits) == 0:
            break

        for sha_object in json_commits:
            sha = sha_object['sha']
            sha_url = 'https://api.github.com/repos/' + repo + '/commits/' + sha
            sha_details, ct = github_auth(sha_url, lst_tokens, ct)
            author = sha_details['commit']['author']['name']
            timestamp = sha_details['commit']['author']['date']
            files_json = sha_details['files']
            for filename_obj in files_json:
                filename = filename_obj['filename']
                dict_files.append([filename, author, timestamp])
                print(filename)
        ipage += 1

# GitHub repo
repo = 'scottyab/rootbeer'

# GitHub token
lstTokens = []

# Dictionary to store files and touched count
dictFiles = []

# Call function to count files
count_files(dictFiles, lstTokens, repo)
print('Total number of files: ' + str(len(dictFiles)))

# Output CSV file
fileOutput = 'data/file_AuthorDateFiles.csv'
rows = ["File", "Author", "Timestamp"]

# Write data to CSV
with open(fileOutput, 'w', newline='') as fileCSV:
    writer = csv.writer(fileCSV)
    writer.writerow(rows)
    writer.writerows(dictFiles)