import json
import requests
import csv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date

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

    # try:
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
            authorName = shaDetails['commit']['author']['name']
            dateTouched = shaDetails['commit']['author']['date']
            dateTouched = dateTouched.replace("T", " ")
            dateTouched = dateTouched.replace("Z", "")
            for filenameObj in filesjson:
                filename = filenameObj['filename']
                if ".java" in filename:
                    authors.append(authorName)
                    files.append(filename)
                    newDate = datetime.strptime(dateTouched, '%Y-%m-%d %H:%M:%S')
                    days = newDate - initialCommit
                    weeks = days.days / 7
                    dates.append(weeks)
                    dictfiles[filename] = 0
        ipage += 1
    # except:
    #     print("Error receiving data")
    #     exit(0)
# GitHub repo
repo = 'scottyab/rootbeer'
# repo = 'Skyscanner/backpack' # This repo is commit heavy. It takes long to finish executing
# repo = 'k9mail/k-9' # This repo is commit heavy. It takes long to finish executing
# repo = 'mendhak/gpslogger'


# put your tokens here
# Remember to empty the list when going to commit to GitHub.
# Otherwise they will all be reverted and you will have to re-create them
# I would advise to create more than one token for repos with heavy commits
lstTokens = ["gvjgvjj"]

dictfiles = dict()
authors = []
files = []
newFiles = []
dates = []
colors = []
initialCommit = datetime(2015, 6, 17)
countfiles(dictfiles, lstTokens, repo)
# print('Total number of files: ' + str(len(files)))

Matthew = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Scott = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Slim = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Fi5t = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
matt = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Daniel = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Ivan = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
matthew = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
altvnv = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Frieder = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Ali = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Leon = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Frieder = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
vyas = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Andy = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
Mohammed = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
mat = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]
leocad = [np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.random.rand(),1), np.round(np.clip(np.random.rand(), 0, 1), 1)]

for author in authors:
    if "Matthew" in author:
        colors.append(Matthew)
    elif "Scott" in author:
        colors.append(Scott)
    elif "Slim" in author:
        colors.append(Slim)
    elif "Fi5t" in author:
        colors.append(Fi5t)
    elif "matt" in author:
        colors.append(matt)
    elif "Daniel" in author:
        colors.append(Daniel)
    elif "Ivan" in author:
        colors.append(Ivan)
    elif "matthew" in author:
        colors.append(matthew)
    elif "altvnv" in author:
        colors.append(altvnv)
    elif "Frieder" in author:
        colors.append(Frieder)
    elif "Ali" in author:
        colors.append(Ali)
    elif "Leon" in author:
        colors.append(Leon)
    elif "vyas" in author:
        colors.append(vyas)
    elif "Andy" in author:
        colors.append(Andy)
    elif "Mohammed" in author:
        colors.append(Mohammed)
    elif "mat" in author:
        colors.append(mat)
    elif "leocad" in author:
        colors.append(leocad)

count = 1
for file in files:
    if dictfiles[file] == 0:
        dictfiles[file] = count
        count += 1

for file in files:
    newFiles.append(dictfiles[file])

plt.scatter(newFiles, dates, c=colors, marker='s')
plt.show()