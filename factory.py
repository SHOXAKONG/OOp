from computer import Computer

class Factory:
    total_count = 0

    def __init__(self, name):
        self.name = name
        self.products = []
        Factory.total_count += 1

    @classmethod
    def get_total_products(cls):
        return cls.total_count

    def add_product(self, product):
        if not isinstance(product, Computer):
            raise TypeError("Faqat komputer qo'shish mumkin")
        self.products.append(product)

    def list_product(self):
        return [product.display_info() for product in self.products]