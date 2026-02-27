a=[11,2,3,4,5,6,7,8,9,10]
b=list(filter(lambda x: x%2==0,a))
c=list(map(lambda x: x*2,a))
e=sorted(a,key=lambda x: x)
print(e)
print(b)
print(c)