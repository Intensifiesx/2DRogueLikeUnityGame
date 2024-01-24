import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def plot_scatter(authors_data):
    colors = {}
    color_counter = 0

    for file, author_dates in authors_data.items():
        for author, date_str in author_dates:
            if author not in colors:
                colors[author] = color_counter
                color_counter += 1

            date_obj = datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')
            week_number = date_obj.strftime('%U')

            plt.scatter(int(week_number), file, c=colors[author], label=author)

    plt.xlabel('Weeks')
    plt.ylabel('Files')
    plt.legend()
    plt.show()


authors_data = {}  #huh??

plot_scatter(authors_data)
