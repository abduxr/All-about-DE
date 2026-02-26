a=[0,2,3,0,0,20,2,0,22,0,33,0]
for i in a:
    if i==0:
        a.remove(i)
        a.append(i)
print(a)    
