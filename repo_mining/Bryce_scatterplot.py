import numpy as np
import matplotlib.pyplot as plot
from datetime import datetime
import csv
import random



def parse_csv():
    data_list = []
    csv_filepath = "./data/file_author_touchesrootbeer.csv"
    with open(csv_filepath, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data_list.append(dict(row))
    return data_list

def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def scatter_plot():
    colors = {}
    legend = {}
    file_count = {}
    file_counter = 0
    data = parse_csv()
    for item in data:
        filename = item["Filename"]
        author = item["Author"]
        date = item["Date"]
        if author not in colors:
            colors[author] = generate_random_color()
        if filename not in file_count:
            file_count[filename] = file_counter
            file_counter += 1
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
        week_number = date_obj.isocalendar()[1]
        if author not in legend:
            legend[author] = 0
            plot.scatter(week_number, file_count[filename], c=colors[author], label=author)
        plot.scatter(week_number, file_count[filename], c=colors[author])
    
    plot.ylabel('Files')
    plot.xlabel('Weeks')
    plot.legend(loc='upper left', bbox_to_anchor=(0,1))
    plot.show()
    
    
scatter_plot()