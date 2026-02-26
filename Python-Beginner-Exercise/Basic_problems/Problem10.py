# Write a program to count the total number of vowels ($a, e, i, o, u$) present in a given sentence.

def vowels(a):
    count=0
    for i in a:
        if i.lower() in "aeiou":
            count+=1
        else:
            continue
    
    return count


a=input("Enter the String to Check the Vowels count: ")
print(vowels(a))



