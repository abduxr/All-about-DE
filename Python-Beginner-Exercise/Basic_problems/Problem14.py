#Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.


def get_list(n):
    b=[]
    for i in range(n):
        try:
            v=int(input("Enter the element of the first array: "))
            b.append(v)
            p=int(input("Enter the element of the second array: "))
            b.append(p)
        except:
            print("Error")
    return b

def even_odd_list(m):
    f=[]
    for i in m:
        if(m.index(i)%2!=0 and i%2!=0 ):
            f.append(i)
        elif (i%2==0):
            f.append(i)
        else:
            continue
    return f

n=int(input("Enter the array size: "))
l=get_list(n)
print(even_odd_list(l))




  