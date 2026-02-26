#Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.
a=[1,2,3,5]
b=[1,3,4,5]
if a[0] == b[0] and a[len(a)-1] == b[len(b)-1]:
    print(True)
else:
    print(False)