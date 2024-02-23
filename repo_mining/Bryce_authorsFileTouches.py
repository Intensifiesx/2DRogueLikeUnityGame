import json
import requests
import csv
from datetime import datetime

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
def countfiles(dictfiles, lsttokens, repo):
    ipage = 1  # url page counter
    ct = 0  # token counter
    counter = 0
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
                repoUrl = 'https://api.github.com/repos/' + repo
                repoDetails, ct = github_auth(repoUrl, lsttokens, ct)
                creation_date = repoDetails['created_at']
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    commitjson = shaDetails['commit']
                    authorjson = commitjson['author']
                    name = authorjson['name']
                    date = authorjson['date']
                    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                    creation_date_obj = datetime.strptime(creation_date, '%Y-%m-%dT%H:%M:%SZ')
                    diff = date_obj - creation_date_obj
                    week = diff.days // 7
                    tuple = (filename,name,week)
                    dictfiles[counter] = tuple
                    counter+=1
                    print(tuple)
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
lstTokens = ["temp"] #Needs to be replaced with github token to work

dictfiles = dict()
countfiles(dictfiles, lstTokens, repo)
print('Total number of Touches: ' + str(len(dictfiles)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_author_touches' + file + '.csv'
rows = ["Touch Index", "Filename", "Author", "Week"]
fileCSV = open(fileOutput, 'w')
writer = csv.writer(fileCSV)
writer.writerow(rows)

for filename, tuple in dictfiles.items():
    rows = [filename, tuple[0], tuple[1], tuple[2]]
    writer.writerow(rows)
fileCSV.close()
#print('The file ' + bigfilename + ' has been touched ' + str(bigcount) + ' times.')
