import numpy as np
import matplotlib.pyplot as plt
import pyarrow
import pandas as pd

#csv contains: (date, (author, filename))
csv = pd.read_csv('data/file_rootbeer_contributors.csv')

#dicts or hashmaps
fileid = {}
authid = {}

def calcWeeks(date):
    _date = date.split('-')

    years = int(_date[0])
    months = int(_date[1])
    days = int(_date[2])
    
    years -= 2015
    months -= 6
    days -= 19

    return (years * 52) + (months * 4) + (days / 7)

#array of tuples = [(date, unique file id, unique author id)]
data = []
#search by employeeid, returns number of commits
numOfCommits = []
#query with a number and a name will be returned
employeeid = []
lastCommit = []
authnum = 0
filenum = 0

for index, row in csv.iterrows():
    date = row['Date'].split('T')[0]

    auth = row['CommitDetails'].split('\'')[1]
    if (auth not in authid):
        authid[auth] = authnum
        employeeid.append(auth)
        authnum += 1

    try:
        numOfCommits[authid[auth]] += 1
    except IndexError:
        numOfCommits.append(1)

    weeks = calcWeeks(date)

    try:
        lastCommit[authid[auth]] = weeks if weeks > lastCommit[authid[auth]] else lastCommit[authid[auth]]
    except IndexError:
        lastCommit.append(weeks)

    filename = row['CommitDetails'].split('\'')[3]
    if (filename not in fileid):
        fileid[filename] = filenum
        filenum += 1

    data.append((weeks, authid[auth], fileid[filename]))

for index in range(authnum):
    print (index, employeeid[index], numOfCommits[index], lastCommit[index])

cmap = plt.cm.get_cmap('hsv', len(authid) + 5)

uniquenames = {}

for row in data:
    plt.scatter(row[2], row[0], c = cmap(row[1]), 
                label = employeeid[row[1]] if employeeid[row[1]] not in uniquenames else "")

    uniquenames[employeeid[row[1]]] = True

# plt.scatter(xAxis, yAxis, c=colors)

plt.xlabel('file')
plt.ylabel('weeks')

plt.legend()


plt.show()
