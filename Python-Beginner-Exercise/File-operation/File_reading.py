#Write a Python program to read the entire contents of a text file named “sample.txt” and print it to the console.
try: 
    with open('sample.csv','r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print("error")


