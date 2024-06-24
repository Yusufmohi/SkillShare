class IceCream:
    def __init__(self):
        self.scoop= 4
        
    def eat(self,scoops):
        self.scoop -= scoops
        if scoops>self.scoop:
            print("Not enough bite left")
        else:
            print(self.scoop)

    def add(self,scoops):
        self.scoop += scoops
