import matplotlib.pyplot as plt
import numpy as np
import csv
import datetime

author = []
# uniqueAuthor = []
date = []
fileName = []
# uniqueFile = []

file = "scottyab/rootbeer".split('/')[1]
# change this to the path of your file
fileOutput = 'data/file_' + file + '.csv'
fileCSV = open(fileOutput, 'r', newline='')
reader = csv.reader(fileCSV, delimiter=',')
next(reader)
for row in reader:
    fileName.append(row[0])
    author.append(row[1])
    date.append(row[2])
fileCSV.close()

uniqueAuthor = list(set(author))
uniqueFile = list(set(fileName))

fullyear = []
week1 = []
form = '%Y-%m-%dT%H:%M:%SZ'
for row in date:
    week1.append(int(datetime.datetime.strptime(row, form).strftime("%W")))
    fullyear.append(int(datetime.datetime.strptime(row, form).strftime("%Y")))

firstYear = fullyear[-1]
year = []
for row in fullyear:
    year.append(row - firstYear)

week = []
for row in range(len(year)):
    week.append(week1[row] + year[row]*52 - week1[-1] + 1)
    # week2.append((1+year[row])*52 - week1[-1])

# for touch in range(len(fileName)):

y = np.random.random(len(author))

plt.scatter(fileName, week, c=y) # s is a size of marker 
plt.xlabel("file")
plt.ylabel("weeks")



plt.show()
