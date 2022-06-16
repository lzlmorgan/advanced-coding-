from dunder_method import Product #parent class/base class

#child class/derived class
class Drink(Product):
	pass

d = Drink('soba', 100)
print(d.name)

