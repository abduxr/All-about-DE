#Print a downward half-pyramid pattern using stars (*).
a=10
b=a
for i in range(a):
    for j in range(b):
        print("*",end=" ")
    b-=1
    print("\n")

