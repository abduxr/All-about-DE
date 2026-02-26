#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
def post_check():
    a=int(input("Enter the array size: "))
    b=[]
    d=[]
    for i in range(a):
        c=int(input("Enter the first array element value: "))
        e=int(input("Enter the second array element value: "))
        b.append(c)
        d.append(e)

    if(b[0]==d[0] and b[a-1] == d[a-1]):
        return True
    else:
        return False
    

cond=post_check()
print(cond)

