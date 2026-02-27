d1 = {"a": 10, "b": 20}
d2 = {"b": 5, "c": 15}

result=d1.copy()

for i in d2.items():
    if i[0] in result:
       d1[i[0]]+=i[1]
    else:
        d1[i[0]]=i[1]  
print(d1)


    