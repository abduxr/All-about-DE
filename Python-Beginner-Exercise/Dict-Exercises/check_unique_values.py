#Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.

def check_unique_value(d):
    a=[]
    for i in d.values():
        if i in a:
            return False
        else:
            a.append(i)
    return True

n=int(input("Enter the size of the Dictionary: "))
d={}
for i in range(n):
    key=input("Enter the key:")
    value=input("Enter the value:")
    d[key]=value    

print(check_unique_value(d))