class IceCream:
    max_scoops=3
    def __init__(self):
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
        self.sold=0
    def order(self,scoop):
        ice=IceCream()
        self.add(ice,scoop)
        return ice
    def add(self,ice,scoop):
        ice.add(scoop)
        self.sold += scoop
