#Write a script that takes a list containing duplicate items and returns a new list with only unique elements
a=[1,2,3,4,52,1,2,34,1,2,34,5]
b=set()
for i in a:
    b.add(i)

print(b)