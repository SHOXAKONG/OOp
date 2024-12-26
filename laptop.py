from computer import Computer

class Laptop(Computer):
    def __init__(self, brand, model, year, price, battery_life):
        super().__init__(brand, model, year, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"Laptop: {self.brand}, {self.model}, {self.year}, {self.price}, {self.battery_life}"
