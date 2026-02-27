#Write a program to check if a given number is a palindrome (reads the same forwards and backwards)
a=int(input("Enter the Number: "))
n=a
p=0
while(n!=0):
    r=n%10
    p=10*p + r
    n=n//10
print(p)
if(a==p):
    print("Yes It is a palindrome")
else:
    print("Not a palindorme")