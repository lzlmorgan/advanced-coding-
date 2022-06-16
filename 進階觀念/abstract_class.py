#abstract class  抽象類別
#抽象class無法做出實力instance
#抽象class用來給人繼承的 base class
#抽象class只有declare沒有content
#抽象class 需要import abc
#有一個或以上的@abstract method

from abc import ABCMeta, abstractmethod #abstract base class

class Product(metaclass=ABCMeta): #BASE
	@abstractmethod
	def hi(self):
		pass

	@abstractmethod
	def hi2(self):
		pass

class Drink(Product):
	def hi(self): #override 第一個抽象class
		print('hi')

	def hi2(self):
		print('hi2')


#p = Product()
d = Drink()