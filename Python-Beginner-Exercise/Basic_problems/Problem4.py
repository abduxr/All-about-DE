#Write a Python code to remove characters from a string from 0 to n and return a new string.

def remove(b,c):
    d=len(b)
    return b[:-1]



a=input("Enter the String: ")
b=int(input("Enter the remova index: "))
b=remove(a,b)
print(b)



