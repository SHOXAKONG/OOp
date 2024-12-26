from computer import Computer
from  factory import Factory
from monoblock import Monoblock
from laptop import Laptop

monoblock1 = Monoblock("HP", "ProOne", 2024, 600, 23.0)
laptop1  = Laptop("lonovo", "IdeaPad", 2023, 500, 75)

factory = Factory("Tech Factory")
factory.add_product(monoblock1)
factory.add_product(laptop1)

print(f"Computer: {Computer.get_total_computer()}")
print(f"Factory: {Factory.get_total_products()}")
print("Factory Products")
for product in factory.list_product():
    print(product)

try:
    laptop1.price = -100
except ValueError as e:
    print(e)

print(monoblock1 > laptop1)