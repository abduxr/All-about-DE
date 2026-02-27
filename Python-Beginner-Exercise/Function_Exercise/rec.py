def sum(num):
    if num:
        return num + sum(num-1)
    else:
        return 0    
    
print(sum(12))