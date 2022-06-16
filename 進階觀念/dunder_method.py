#__name__

class Product:
	def __init__(self, name, price):
		self.name = name #property
		self.price = price #property

	# # __str__決定如何print 簡易版
	# def __str__(self): 
	# 	#return self.name + ': $' + str(self.price)
	# 	return f'{self.name}: ${self.price}' #f string輸出

	# #representation 最完整輸出print
	# def __repr__(self): 
	# 	return f'<Product({self.name}, {self.price})>'

p = Product('bublle tea', 60) #創建class類,然後建立class的實例instance
print(p)
print(repr(p))