class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_info(self):
        print(f"The Name of the boy is {self.name} and his age is {self.age}")

s1=student("Abdullah",21)
s1.print_info()
