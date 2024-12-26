from abc import ABC, abstractmethod

class Computer:
    total_count = 1

    def __init__(self ,brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self._price = price
        Computer.total_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self._price = value

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computer(cls):
        return cls.total_count

    def __gt__(self, other):
        if not isinstance(other, Computer):
            return NotImplemented
        return self._price > other.price