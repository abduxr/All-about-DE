#Write a program to find how many times the substring “Emma” appears in a given string.
flag=0
child = "Emma"
parent = "Emma is a Emma and emma is a Emma of Emma"
a=parent.split(" ")
for i in a:
    if(child==i):
        flag+=1
print(flag)


'''
child="emma"
parent="Emma is a Emma and emma is a Emma of Emma"
print(parent.count(child))
'''