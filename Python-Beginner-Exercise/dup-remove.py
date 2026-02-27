#Given a list, remove duplicates while maintaining order.
a=[1,2,3,2,3,4,5,4,5,5,6,7,8,9,10]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        continue

print(b)
