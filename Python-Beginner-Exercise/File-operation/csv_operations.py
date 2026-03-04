import csv 

try:
    with open('sample.csv','r') as file:
        data=csv.reader(file)
        for i in data:
            print(i)
except Exception as e:
    print('Error: ',e)

    
