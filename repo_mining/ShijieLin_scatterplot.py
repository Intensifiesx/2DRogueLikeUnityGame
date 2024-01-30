# Lib
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# Read data from csv
data = pd.read_csv('commit_records.csv')
data = data.dropna(subset=['Touched Files'])
data['Commit Date'] = pd.to_datetime(data['Commit Date']).dt.date

# Ensure 'Author' column exists and contains no NaN values
if 'Author' in data.columns:
    data = data.dropna(subset=['Author'])
else:
    raise ValueError("The data does not contain an 'Author' column.")

# get all authors
unique_author = data['Author'].unique()

# map the color to authors
color_map = plt.get_cmap('tab20')
num_colors = color_map.N

# Create a mapping from author to color, cycling through the color map if necessary
author_to_color = {author: color_map(i % num_colors) for i, author in enumerate(unique_author)}

# Calculate the number of weeks since the baseline date
baseline_date = datetime.strptime('2015-06-19', '%Y-%m-%d').date()
data['Weeks'] = data['Commit Date'].apply(lambda x: (x - baseline_date).days // 7)

# Map files to IDs
touched_files = data['Touched Files']
file_to_id = {}
for files in touched_files.str.split(';'):
    for file in files:
        if file not in file_to_id:
            file_to_id[file] = len(file_to_id)

# Create the plot
plt.figure(figsize=(10, 6))

# recored unique authors
added_labels = set()

for _, row in data.iterrows():
    author = row['Author']
    week = row['Weeks']
    for file in str(row['Touched Files']).split(';'):
        file_id = file_to_id[file]
        if author not in added_labels:
            plt.scatter(file_id, week, color=author_to_color[author], marker='x', label=author)
            added_labels.add(author)
        else:
            plt.scatter(file_id, week, color=author_to_color[author], marker='x')

plt.xlabel('File Index')
plt.ylabel('Weeks')
plt.title('Commit Activity Over Time')
plt.legend(title="Authors", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()