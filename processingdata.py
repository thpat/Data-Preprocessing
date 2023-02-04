import csv
import json

with open("percapita_flat.csv", mode= 'r', encoding= "utf8" ) as file:
    csv_file = csv.DictReader(file)
    lst = list(csv_file)
    print(json.dumps(lst, ident=4))