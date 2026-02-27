#Print a multiplication table from 1 to 10 in a formatted grid.
a=30
for i in range(1,20):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("**********")

