class Light:
    def __init__(self,sync=None):
        super().__init__()
        self.on=False
        self.sync=sync
    def toggle(self):
        self.on=not self.on
        if self.sync is not None:
            self.sync.toggle()

class oldlight(Light):
    def __init__(self,sync=None):
        super().__init__(sync=sync)
        self.on=False
        self.sync=sync
        self.flicker=False
    def toggle(self):
        super().toggle()
        if self.on:
            self.flicker= not self.flicker

class Timer:
    def __init__(self):
        self.left=0
    def set(self,left):
        self.left=left
    def ring(self):
        print("Timer is Up!!")
    def elapse(self,t):
        if self.left>0:
            self.left=max(self.left-t,0)
            if self.left==0:
                self.ring()

class TimerLight(Light,Timer):
    def set(self,left):
        super().set(left)
        if self.left>0:
            self.on=True
    def ring(self):
        super().ring()
        self.on=False
