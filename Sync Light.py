class Light:
    def __init__(self,sync=None):
        self.on=False
        self.sync=sync
    def toggle(self):
        self.on=not self.on
        if self.sync is not None:
            self.sync.toggle()
