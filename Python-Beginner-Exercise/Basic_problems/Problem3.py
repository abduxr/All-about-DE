#Write a Python code to accept a string from the user and display characters present at an even index number.
a=input("Enter a random String: ")
for i in range(len(a)):
    if(i%2==0):
        print(f"Even index {i} Character = {a[i]}")
