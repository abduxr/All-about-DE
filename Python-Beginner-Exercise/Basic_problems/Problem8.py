#Print the following pattern where each row contains a number repeated a specific number of times based on its value.
i=1
a=int(input("enter the range: "))
for i in range(a):
    for j in range(i):
        print(j,end=" ")
    print(end="\n")