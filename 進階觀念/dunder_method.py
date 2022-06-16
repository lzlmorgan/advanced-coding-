#__name__

class Product:
	def __init__(self, name, price):
		self.name = name #property
		self.price = price #property

	# __str__決定如何print 簡易版
	def __str__(self): 
		#return self.name + ': $' + str(self.price)
		return f'{self.name}: ${self.price}' #f string輸出

	#representation 最完整輸出print
	def __repr__(self): 
		return f'<Product({self.name}, {self.price})>'

	def __add__(self, other):
		if isinstance(other, str):
			self.name += other
		if isinstance(other, Product):
			return [self, other]

	def __mul__(self, other):
		re = []
		if isinstance(other, int): #創建實例instance other是int
			for i in range(other):
				re.append(self)
		return re


#p = Product('bublle tea', 60) #創建class類,然後建立class的實例instance
#p + ' cream'
#print(p)
#print(repr(p))
p1 = Product('ramen', 60)
p2 = Product('tea', 200)
# print(p1 + p2) #清單+清單=清單
print(p1*5)