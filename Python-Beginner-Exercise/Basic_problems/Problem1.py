#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
a = int(input("Enter the first number: "))
b = int(input("Enter the Secind number: "))

if(a*b>=1000):
    print(a+b)
else:
    print(a*b)
