class IceCream:
    max_scoops=3
    def __init__(self):
        ice=super().__init__()
        self.scoop=0
    def eat(self,scoop):
        if self.scoop<scoop:
            print("Not Enough Bite left!")
        else:
            self.scoop -= scoop
    def add(self,scoop):
        self.scoop += scoop
        if self.scoop>self.max_scoops:
            self.scoop=0
            print("Max number of SCOOPS!!")

class IceCreamTruck:
    def __init__(self):
        ice=super().__init__()
        self.sold=0
    def order(self,scoop):
        ice=IceCream()
        self.add(ice,scoop)
        return ice
    def add(self,ice,scoop):
        ice.add(scoop)
        self.sold += scoop

class DeluxeIceCreamTruck(IceCreamTruck):
    def order(self,scoop):
        ice=super().order(scoop)
        ice.add(1)
        return ice


class Drinkable:
    def __init__(self):
        self.cup=0
    def add(self,cup):
        self.cup += cup
    def drink(self,cup):
        self.cup -= cup

class Lemonade(Drinkable):
    pass

class MeltingIceCream(IceCream,Drinkable):
    def elapse(self,t):
        melted=min(t,self.scoop)
        self.scoop -= melted
        self.cup += melted
