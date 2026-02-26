a={}
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for i in words:
    c=words.count(i)
    a[i]=c
for key,value in a.items():
    print(value,end=" ")
sorted=dict(sorted(a.items(),key=lambda x: x[1],reverse=True))
print(sorted)
print(a)