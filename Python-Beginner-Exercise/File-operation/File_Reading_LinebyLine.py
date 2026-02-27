#Write a Python program to read the text file named “sample.txt” line by line and print each line.
try:
    with open ('sample.csv','r') as file:
         print(file.readline().strip())
         print(file.readline().strip())
except Exception as e:
    print("Error: ",e)
