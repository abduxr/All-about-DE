import json
try:
    with open('sample.json','r') as file:
        data=json.load(file)
        for i in data:
            print(i)

except Exception as e:
    print('Error: ',e)

