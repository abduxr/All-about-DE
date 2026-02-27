#Write a program to extract each digit from an integer in the reverse order.

n=int(input("Enter the number to be reversed: "))
m=0
while(n!=0):
    m=10*m+(n%10)
    n=n//10

print(m)