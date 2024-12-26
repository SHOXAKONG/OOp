from computer import Computer


class Monoblock(Computer):
    def __init__(self, brand, model, year, price, screen_size):
        super().__init__(brand, model, year, price)
        self.screen_size = screen_size

    def display_info(self):
        return f"Monoblock: {self.brand}, {self.model}, {self.year}, {self.price}, {self.screen_size}"