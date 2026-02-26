a=[1,2,2,3,3,3,4]
b={}
flag=0
for i in a:
    for j in a:
        if i==j:
            flag+=1
    b[i]=flag
    flag=0
print(b)    


