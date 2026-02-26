#Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

a=0
b=1
print("0 1",end=" ")
n=10
for i in range(n):
    d=a+b
    print(d,end=" ")
    a=b
    b=d