#Calculate income tax for a given income based on these rules:
salary=int(input("please enter your salary: "))
t1=0
tax=0
if(salary<=10000):
    tax=salary*(10/100)
    print(tax)
elif(salary>10000 and salary <=20000 ):
    salary=salary-10000
    tax=salary*(10/100)
    print(f"Tax={(tax+1000.0)}")
else:
    salary=salary-20000
    tax=salary*(20/100)
    print(f"Tax= {(tax+2000)}")

    

