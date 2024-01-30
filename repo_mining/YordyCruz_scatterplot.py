import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import numpy as np
from datetime import datetime
import matplotlib.dates as mdates


# Input and output file
input_file = 'data/authorsFileTouches.csv' 
output_file = 'scatterplot.png'

# Read the CSV file
df = pd.read_csv(input_file)

# Get the requirement Filename, Author, and Date columns
required_columns = ['Filename', 'Author', 'Date']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise KeyError(f"The following required columns are missing from the input CSV file: {', '.join(missing_columns)}.")

# Convert the Date column to objects
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the number of weeks
start_date = df['Date'].min()
df['Weeks_Since_Start'] = df['Date'].apply(lambda x: ((x - start_date).days) // 7)

# Assign each file a unique index
file_to_index = {file: i for i, file in enumerate(df['Filename'].unique())}
df['File_Index'] = df['Filename'].map(file_to_index)

# Assign a unique color to each author
authors = df['Author'].unique()
color_map = get_cmap('nipy_spectral')
author_to_color = {author: color_map(i / len(authors)) for i, author in enumerate(authors)}

# Create the scatter plot with a larger figure size
plt.figure(figsize=(15, 10)) 

for author in authors:
    author_data = df[df['Author'] == author]
    plt.scatter(author_data['File_Index'], author_data['Weeks_Since_Start'],
                color=author_to_color[author], label=author, s=40, alpha=0.7)

# Customize the plot
plt.xlabel('File Index')
plt.ylabel('Weeks Since Start')
plt.title('File Touches Over Time by Author')
plt.legend(title='Author', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='x-small')

# Improve readability for the plot
plt.gca().xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)  # Rotate the date labels for better fit

# Set y-axis limit
plt.ylim([-10, df['Weeks_Since_Start'].max() + 10])

# Determine the step size for x-axis ticks
step_size = len(file_to_index) // 10 # set index number
step_size = max(1, step_size)  # Ensure step size is at least 1

# Set x- to display file
plt.xticks(ticks=np.arange(0, len(file_to_index), step_size), labels=np.arange(0, len(file_to_index), step_size))

# Adjust plot margins
plt.margins(y=0.1)
plt.subplots_adjust(right=0.8)

# Save and show the plot
plt.tight_layout()
plt.savefig(output_file, dpi=300)
plt.show()