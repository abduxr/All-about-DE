d = {"a": 1, "b": 2, "c": 3}
c={}
for i in d.items():
    c[i[1]]=i[0]
print(c)
