class Light:
    def __init__(self):
        self.on=False
        
    def toggle(self):
        if self.on==False:
            self.on=True
        else:
            self.on=False
    

r=Light()
t=Light()
