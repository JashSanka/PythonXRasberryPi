import csv

with open("test.csv", newline="") as csvfile:
    line=csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in line:
        print(", ".join(row))
