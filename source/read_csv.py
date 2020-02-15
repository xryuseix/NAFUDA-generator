import csv
import os

def read_csv():
    dictdata = []
    with open(os.getcwd() + "/storage/csv_files/data.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            dictdata.append(row)

    return dictdata

# Usage
# csv = read_csv()
# print(csv[1]['ユーザー名'])