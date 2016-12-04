
import csv

processed_csv = open('pre-processed.csv', 'wb')
csv_writer = csv.writer(processed_csv)

with open('unseen_data_set_1.csv', 'rb') as cfile:
    cfile_reader = csv.reader(cfile)
    for row in cfile_reader:
        if ' ?' not in row and ' United-States' in row:
            csv_writer.writerow(row)
processed_csv.close()

