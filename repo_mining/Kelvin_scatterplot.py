import numpy as np
import matplotlib.pyplot as plt
import pyarrow
import pandas as pd

#csv contains: (date, (author, filename))
csv = pd.read_csv('data/file_rootbeer_contributors.csv')

#dicts or hashmaps
fileID = {}
authID = {}

#finds number of weeks since repo was created compared to commit date
def calcWeeks(date, repoInitDate):
    _date = date.split('-')
    _repoInitDate = repoInitDate.split('-')

    years = int(_date[0])
    months = int(_date[1])
    days = int(_date[2])
    
    years -= int(_repoInitDate[0])
    months -= int(_repoInitDate[1])
    days -= int(_repoInitDate[2])

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

firstCommit = csv['Date'][len(csv) - 1].split('T')[0]

#parse csv getting who the author is, which file was interacted with, and when it was modified
for index, row in csv.iterrows():
    date = row['Date'].split('T')[0]

    auth = row['CommitDetails'].split('\'')[1]
    #check for unique contributor/author, assign a new ID if new author
    if (auth not in authID):
        authID[auth] = authnum
        employeeid.append(auth)
        authnum += 1

    #tracks number of commits by author ID
    try:
        numOfCommits[authID[auth]] += 1
    #if its a new author, allocate slot for them
    except IndexError:
        numOfCommits.append(1)

    #weeks since repo was created
    weeks = calcWeeks(date, firstCommit)

    #track an authors' most recent commit to the repo
    try:
        lastCommit[authID[auth]] = weeks if weeks > lastCommit[authID[auth]] else lastCommit[authID[auth]]
    #if new author, again track by their author ID
    except IndexError:
        lastCommit.append(weeks)

    #check if the file being modified is new or not
    filename = row['CommitDetails'].split('\'')[3]
    if (filename not in fileID):
        fileID[filename] = filenum
        filenum += 1

    data.append((weeks, authID[auth], fileID[filename]))

table = {}
#print informantion to view
for index in range(authnum):
    table[index] = [employeeid[index], numOfCommits[index], lastCommit[index]]

#view terminal to see the table
df = pd.DataFrame.from_dict(table, orient='index', columns=['Name', 'Commits', 'Latest Commit'])

df = df.rename_axis(index='ID')

print(df)

cmap = plt.cm.get_cmap('hsv', len(authID) + 5)

uniquenames = {}

#plot on a scatterplot
for row in data:
    plt.scatter(row[2], row[0], color = cmap(row[1]), 
                label = employeeid[row[1]] if employeeid[row[1]] not in uniquenames else "")

    uniquenames[employeeid[row[1]]] = True

plt.xlabel('file')
plt.ylabel('weeks')

plt.legend()


plt.show()
