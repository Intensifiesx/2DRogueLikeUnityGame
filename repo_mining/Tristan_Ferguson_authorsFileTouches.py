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
# @dictDate, empty dictionary of dates
# @dictAuthor, empty dictionary of authors
# @lstTokens, GitHub authentication tokens
# @repo, GitHub repo
def countfiles(dictfiles, nameList, dateList, authorList, lsttokens, repo):
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
                date = shaDetails['commit']['author']['date']
                author = shaDetails['commit']['author']['name']
                filesjson = shaDetails['files']
                #funny coding moment
                for filenameObj in filesjson:
                    filename = filenameObj['filename']
                    # author = filenameObj['author']
                    # date = filenameObj['date']
                    # dictfiles[filename] = dictfiles.get(filename, 0) + 1
                    # dictfiles[author] = dictfiles.get(author, 0) + 1
                    # dictfiles[date] = dictfiles.get(date, 0) + 1
                    nameList.append([filename, author, date])
                    # dictfiles.append([filename, author,date])
                    # authorList.append(author)
                    # dateList.append(date)

                    

                    print(filename)
                # for authorObj in authorjson:
                #     dictauthor[author] = dictauthor.get(author,0) + 1
                # for dateObj in datejson:
                #     dictdate[date] = dictdate.get(date, 0) + 1

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
lstTokens = ["funnyToken"]

nameList = []
authorList = []
dateList = []
dictfiles = []

countfiles(dictfiles, nameList, authorList, dateList, lstTokens, repo)
print('Total number of files: ' + str(len(nameList)))

file = repo.split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '.csv'
rows = ["Filename", "Author", "Time"]
fileCSV = open(fileOutput, 'w', newline='')
writer = csv.writer(fileCSV)
writer.writerow(rows)

writer.writerows(nameList)

fileCSV.close()