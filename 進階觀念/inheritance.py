from dunder_method import Product #parent class/base class

#child class/derived class
class Drink(Product):
	def __init__(self, name, price, volume): 
		super().__init__(name, price) #supper().__init__可以呼叫到parent的class
		self.volume = volume 

d = Drink('Tekila', 100, 600)
print(d.volume)
print('--------------------')
print(type(d)) #instance實例d的class資料類別
print(isinstance(d, Drink))#判斷d是不是屬於class Drink的類別
print(isinstance(d, Product)) ##判斷d是不是屬於class Product的類別
print(type(Drink))

