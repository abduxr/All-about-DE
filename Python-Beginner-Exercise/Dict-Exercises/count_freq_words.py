a={}
f= ["Apple", "Banana", "Mango", "Orange", "Grapes", "Pineapple"]

for i in f:
    n=len(i)
    if n not in a:
        a[n]=[i]
    else:
        a[n].append(i)
print(a)

