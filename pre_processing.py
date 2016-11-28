
import csv

processed_csv = open('pre-processed.csv', 'wb')
csv_writer = csv.writer(processed_csv)

with open('unseen_data_set_1.csv', 'rb') as cfile:
    cfile_reader = csv.reader(cfile)
    for row in cfile_reader:
        if ' ?' not in row and ' United-States' in row:
            csv_writer.writerow(row)
processed_csv.close()

# missing = open('missing.txt', 'wb')
# outlier = open('outlier.txt', 'wb')
#
# with open('unseen_data_set_1.csv', 'rb') as cfile:
#     cfile_reader = csv.reader(cfile)
#     [missing.write(str(row) + '\n') for row in cfile_reader if ' ?' in row]
# missing.close()
#
# with open('unseen_data_set_1.csv', 'rb') as cfile:
#     cfile_reader = csv.reader(cfile)
#     [outlier.write(str(row) + '\n') for row in cfile_reader if ' United-States' not in row]
# outlier.close()

