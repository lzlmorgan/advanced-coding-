from dunder_method import Product #parent class/base class

#child class/derived class
class Drink(Product):
	def __init__(self, name, price, volume): 
		super().__init__(name, price) #supper().__init__可以呼叫到parent的class
		self.volume = volume 

d = Drink('vodka', 100, 600)
print(d.volume)

