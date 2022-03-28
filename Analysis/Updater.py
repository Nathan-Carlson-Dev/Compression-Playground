class Updater:

    def __init__(self, generator, updater, reset, info):
        self.generator = generator
        self.updater = updater
        self.reseT = reset
        self.info = info

    def generate(self):
        return self.generator(self.info)
    
    def update(self):
        self.updater(self.info)

    def reset(self):
        self.reseT(self.info)