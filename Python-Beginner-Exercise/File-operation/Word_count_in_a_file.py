#Create a function that takes a filename as input and returns the total number of words in that file.
def check(fil,word):
    import re
    count=0
    try:
        with open(fil,'r') as file:
            content=file.read()
            words=re.findall(r'\b\w+\b',content)
            for i in words:
                if word==i:
                    count+=1
            print(count)
    except Exception as e:
        print(f"Error: {e}")


check('sample.txt',"the")