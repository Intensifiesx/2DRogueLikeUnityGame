import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.dates import date2num

file_path = 'data/file_rootbeer_contributors.csv'  #assume grade from the repo
with open(file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# relevant information from the CSV data
filenames = [row['Filename'] for row in data]
authors = [row['OriginalAuthor'] for row in data]
dates = [datetime.strptime(row['LastModifiedDate'], "%Y-%m-%dT%H:%M:%SZ") for row in data]

# a dictionary to map authors to unique colors
unique_authors = list(set(authors))
author_color_mapping = {author: cm.get_cmap('tab10')(i / len(unique_authors)) for i, author in enumerate(unique_authors)}

# a mapping of filenames to file indexes
filename_index_mapping = {filename: i for i, filename in enumerate(filenames)}

# a 2D matrix to represent the scatter plot
weeks = [(date - min(dates)).days // 7 for date in dates]
scatter_matrix = [[-1 for _ in range(len(filenames))] for _ in range(max(weeks) + 1)]

# the scatter matrix with author colors
for filename, author, week in zip(filenames, authors, weeks):
    file_index = filename_index_mapping[filename]
    scatter_matrix[week][file_index] = author_color_mapping[author]

# create scatter plot
fig, ax = plt.subplots(figsize=(10, 6))

# plot the scatter matrix
for week, colors in enumerate(scatter_matrix):
    for file_index, color in enumerate(colors):
        if color != -1:
            ax.scatter(file_index, week, color=color, s=50)

# get the plot
ax.set_xlabel('File Index')
ax.set_ylabel('Weeks')
ax.set_title('Weeks vs File Variables')

# show the plot
plt.tight_layout()
plt.show()
