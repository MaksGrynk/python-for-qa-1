
import csv

with open('csv_example_write1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    header = ['#', 'name', 'description']
    writer.writerow(header)

    for i in range(0, 3):
        name = 'name {}'.format(i)
        description = 'description {}'.format(i)
        writer.writerow([i, name, description])


with open('csv_example_write2.csv', 'w') as csvfile:
    header = ['#', 'name', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=header)

    writer.writeheader()
    writer.writerow({'#': 1, 'name': 'name 1', 'description': 'description 1'})
    writer.writerow({'#': 2, 'name': 'name 2', 'description': 'description 2'})
    writer.writerow({'#': 3, 'name': 'name 3', 'description': 'description 3'})
