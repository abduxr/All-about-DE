#terate through a given list of numbers and print only those numbers which are divisible by 5.
def get_list(n):
    b=[]
    for i in range(n):
        a=int(input("Enter the array element: "))
        b.append(a)
    return b

def div_check(a):
    for i in a:
        if(i%5==0):
            print(i,end=" ")

g=int(input("Enter the array size: "))
b=get_list(g)
div_check(b)
