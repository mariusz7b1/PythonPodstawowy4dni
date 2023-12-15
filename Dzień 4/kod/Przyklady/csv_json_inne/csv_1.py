
import csv
filename = 'd:\\dane\\test.csv'
with open(filename, encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
        for word in row:
            print(word)
