import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Read the data from the CSV file
data = pd.read_csv('authors_file_touches.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Calculate weeks since start of project
start_date = data['Date'].min()
data['Weeks'] = data['Date'].apply(lambda x: (x - start_date).days // 7)

# Shorten file paths to only the last part (filename)
data['ShortFilename'] = data['Filename'].apply(lambda x: x.split('/')[-1])

# Assign unique numbers to shortened filenames for plotting
unique_files = data['ShortFilename'].unique()
file_to_number = {file: i for i, file in enumerate(unique_files)}
data['FileNumber'] = data['ShortFilename'].apply(lambda x: file_to_number[x])

# Assign a unique color to each author
authors = data['Author'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(authors)))
author_color = {author: color for author, color in zip(authors, colors)}

# Create scatter plot
fig, ax = plt.subplots(figsize=(4, 4))  
for author in authors:
    author_data = data[data['Author'] == author]
    ax.scatter(author_data['FileNumber'], author_data['Weeks'], color=author_color[author], label=author, alpha=0.7)

# Format the plot
ax.set_xlabel('Files')
ax.set_ylabel('Weeks Since Start of Project')
ax.set_title('Author File Touches Over Time')

# Rotate the file labels for better readability
plt.xticks(range(len(unique_files)), unique_files, rotation=45, ha='right')

# Set y-axis to show weeks 0 to 250
plt.yticks(range(0, 251, 50))

# Place the legend 
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.2, box.height])  # Resize plot to make space for the legend
ax.legend(title='Authors', loc='center left', bbox_to_anchor=(1, 0.5))


# Adjust layout to fit the legend and labels
plt.tight_layout(rect=[0, 0.1, 1, 1])

# Show the plot
plt.show()

