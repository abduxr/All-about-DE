#Both Write and append operation

try:
    with open('sample.txt','r') as c:
        content=c.read()
    with open('write.txt','a') as file:
        file.write('\n' + content)
except Exception as e:
    print("Error: ",e)