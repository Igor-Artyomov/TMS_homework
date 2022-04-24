import csv
import json


with open('dict_to_json.json', 'r') as f:
    ls = json.load(f)
    id = list(ls.keys())
    data = list(ls.values())
    names = []
    ages = []
    for i in range (len(ls)):
        names.append(data[i][0])
        ages.append(data[i][1])
    phones = ['123-45-67', '252-41-29', '458-78-77', '258-58-89', '325-89-45']

with open("persons.csv", mode="w") as w_file:
    file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
    file_writer.writerow(["id", "name", "age", "phone"])
    for i in range (len(ls)):
        file_writer.writerow([id[i], names[i], ages[i], phones[i]])