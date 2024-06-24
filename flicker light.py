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
