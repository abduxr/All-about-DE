#Iterate through a given list of numbers and print only those numbers which are divisible by 5.
def div(arr):
    for i in arr:
        if(i%5==0):
            print(i)

def printt():
    d=[]
    a=int(input("Enter the array size: "))
    for i in range(a):
        g=int(input("Enter the array elements: "))
        d.append(g)
    div(d)

printt()


