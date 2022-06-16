from dunder_method import Product #parent class/base class

#child class/derived class
class Drink(Product):
	def __init__(self, name, price, volume): 
		super().__init__(name, price) #supper().__init__可以呼叫到parent的class
		self.volume = volume 

d = Drink('Tekila', 100, 600)
print(d.volume)
print(type(d)) #instance實例d的class資料類別
print(isinstance(d, Drink))#判斷d是不是屬於class Drink的類別
print(isinstance(d, Product)) ##判斷d是不是屬於class Product的類別
print(type(Drink)) #class Drink的type是type
print('-----------------------------------------')
print(isinstance(Drink, type)) #class drink是type的實例
print(isinstance(type,object)) #type 是 object的實例
print(isinstance(Drink, object)) #class drink也是object的實例


print('----------------------------------------')
class Food(Product):
	pass

Food = type('Food', (Product,), {})
f = Food('pasta', 220)
print(type(f))

#以上两个表达了同样的意思 创建class food并继承Produc
#type类别 创建出 class 创建出 instance
#class是type的實例instance
#再創建class的實例instance

print('----------------------------------------')




