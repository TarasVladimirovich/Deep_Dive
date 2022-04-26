import csv
from pprint import pprint

with open('example.csv', encoding='utf-8') as file_:
    csv_data = csv.reader(file_)
    data_lines = list(csv_data)

for line in data_lines[:5]:
    print(line)

for line in zip(*data_lines[:5]):
    print(line)
