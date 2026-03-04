class vehicle:
    def __init__(self,veh_name,color,owner):
        self.vehicle=veh_name
        self.color=color
        self.owner=owner
    
    def print_info(self):
        print(f"The name is the vehicle is {self.vehicle}\nThe color of the vehicler is {self.color}\nAnd the Owner of the Vehicle is {self.owner}")

class sub_veh(vehicle):
    pass


v1=vehicle("Ford","Red","Abdullah")
v1.print_info()        


v2 = sub_veh("ROLCE ROYSE","GREY","Arshiya Shafa")
v2.print_info()