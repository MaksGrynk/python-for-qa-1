
import csv


with open('csv_example.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(', '.join(row))

# #, name, description
# 1, name1, description1
# 2, name2, description2
# 3, name3, description3


with open('csv_example.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

# {'#': '1', 'name': 'name1', 'description': 'description1'}
# {'#': '2', 'name': 'name2', 'description': 'description2'}
# {'#': '3', 'name': 'name3', 'description': 'description3'}
