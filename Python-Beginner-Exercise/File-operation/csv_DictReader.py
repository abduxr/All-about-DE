import csv 

with open('sample.txt','r') as file:
    data=csv.DictReader(file)
    for i in data:
        print(i)