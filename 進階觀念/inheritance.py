from dunder_method import Product #parent class/base class

#child class/derived class
class Drink(Product):
	def __init__(self, name, price, volume): #child overwrite the parent
		self.name = name
		self.price = price
		self.volume = volume

d = Drink('vodka', 100, 600)
print(d.volume)

