a=[2,3,2,3,2,3,23,2,6,5,3,6,32456,753,35643,3454]
b=sorted(a,key=lambda x : x)
n=len(b)
print(b[n-2])

a.remove(max(a))
print(max(a))