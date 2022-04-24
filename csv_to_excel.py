import pandas as pd
import csv


with open("persons.csv") as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    id = []
    name = []
    phone = []
    for row in file_reader:
        id.append(row[0])
        name.append(row[1])
        phone.append(row[3])
   

df = pd.DataFrame({
    ' ': [id[0], name[0], phone[0]], 
    'Person 1': [id[1], name[1], phone[1]], 
    'Person 2': [id[2], name[2], phone[2]], 
    'Person 3': [id[3], name[3], phone[3]], 
    'Person 4': [id[4], name[4], phone[4]], 
    'Person 5': [id[5], name[5], phone[5]], 
}
)

df.to_excel('./persons.xlsx', index = False)