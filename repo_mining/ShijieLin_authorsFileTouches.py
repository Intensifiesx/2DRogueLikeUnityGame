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
        headers = {'Authorization': 'Bearer {}'.format(lsttoken[ct])}
        request = requests.get(url, headers=headers)
        jsonData = json.loads(request.content)
        ct += 1
    except Exception as e:
        pass
        print(e)
    return jsonData, ct

# @dictFiles, empty dictionary of files
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(commits_data, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter

    try:
        # loop though all the commit pages until the last returned empty page
        while True:
            spage = str(ipage)
            commitsUrl = 'https://api.github.com/repos/' + repo + '/commits?page=' + spage + '&per_page=100'
            jsonCommits, ct = github_auth(commitsUrl, lsttokens, ct)

            # break out of the while loop if there are no more commits in the pages
            if len(jsonCommits) == 0:
                break

            # iterate through the list of commits in  spage
            for shaObject in jsonCommits:
                sha = shaObject['sha']
                # For each commit, use the GitHub commit API to extract the files touched by the commit
                shaUrl = 'https://api.github.com/repos/' + repo + '/commits/' + sha
                shaDetails, ct = github_auth(shaUrl, lsttokens, ct)
                filesjson = shaDetails['files']
                
                author_name = shaDetails['commit']['author']['name']
                last_modified_date = shaDetails['commit']['author']['date']
                commit_list = [last_modified_date, author_name]
                
                # change the below to get the file with extension u want
                source_extensions = ('.java', '.kt')
                
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    if filename.endswith(source_extensions):
                        commit_list.append(filename)
                        # print(filename)
                        
                commits_data.append(commit_list)
            ipage += 1
    except:
        print("Error receiving data")
        exit(0)
   
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = [""]

# commits_data for store all info
commits_data = []

countfiles(commits_data, lstTokens, repo)

output_filename = 'data/commit_records.csv'

with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(['Commit Date', 'Author', 'Touched Files'])

    # Write the commit data
    for commit in commits_data:
        commit_date = commit[0]
        author_name = commit[1]
        # Join the list of touched files into a single string separated by a semicolon
        touched_files = ';'.join(commit[2:])
        writer.writerow([commit_date, author_name, touched_files])

print(f'Commit records have been saved to {output_filename}.')