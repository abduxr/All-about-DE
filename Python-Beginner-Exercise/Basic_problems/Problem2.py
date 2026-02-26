#Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
a=int(input("Enter the Range number: "))
i=0
for i in range(a):
    if(i<1):
        print(f"Sum of Current Number 0 and Its previous numebr is 0")
        continue
    else:
        print(f"Sum of Current Number {i} and Its previous numebr {i-1} is {i+(i-1)} ")

    
    