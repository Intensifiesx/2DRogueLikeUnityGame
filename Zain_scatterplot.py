import matplotlib.pyplot as plt
import pandas as pd
import csv
import random
from datetime import datetime

with open('data/file_AuthorDateFiles.csv', newline='') as csvfile:
    df = pd.DataFrame(csv.reader(csvfile))
    years = []
    months = []
    days = []
    time = []
    myDict = {}
    uniqueAuthors = set()
    
    # get unique authors
    for i in range(1, len(df[1])):
        uniqueAuthors.add(df[1][i])
        
    # create colors based on number of authors
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(len(uniqueAuthors))]
    
    mySet = set()
    for i in range(1, len(df[1])):
        years.append(df[2][i].split('-')[0])
        months.append(df[2][i].split('-')[1])
        days.append(df[2][i].split('-')[2].split('T')[0])
        time.append(years[i-1] + ' ' + months[i-1] + ' ' + days[i-1])
        mySet.add(df[0][i])
        myDict[df[1][i]] = color[list(uniqueAuthors).index(df[1][i])]
        
    mySet = list(mySet)
    mySet_numbers = list(range(1, len(mySet) + 1))  # Generate numbers for the ticks
    
    # Plot scatter
    fig, ax = plt.subplots()
    numFiles = len(df[0])
    for i in range(1, len(df[0])):
        str = time[i-1]   
        dt1 = datetime.strptime(str, '%Y %m %d')
        str = years[len(years)-1] + ' ' + months[len(months)-1] + ' ' + days[len(days)-1]
        dt2 = datetime.strptime(str, '%Y %m %d')
        weeks_diff = abs((dt2 - dt1).days) // 7
        ax.scatter(weeks_diff, df[0][i], c=myDict[df[1][i]])
    markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in myDict.values()]
    ax.legend(markers, myDict.keys(), numpoints=1, loc='upper right', prop={'size': 6})
    arr = []
    for i in range(1, len(mySet)):
        if i % 10 == 0:
            arr.append(i)
    ax.set_yticks(arr)
    ax.set_yticklabels(arr)
    ax.set_xlabel('Weeks')
    ax.set_ylabel('File')
    
    plt.show()
