import csv


def readCsv(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
#apply filter

#calling function
readCsv('supermarket_sales.csv')

