#animal
#metaclass=ABCMeta強迫繼承屬性的child class必須override抽象class

from abc import ABCMeta,abstractmethod,ABC

class Animal(metaclass=abc.ABCMeta): #metaclass=abc.ABCMeta 可用ABC代替
	@abc.abstractmethod
	def make_sound(self):
		print('assd')
		pass

class Dog(Animal):
	def make_sound(self):
		print('bark')

class Cat(Animal):
	def make_sound(self):
		print('meow')

class Person(Animal):
	def make_sound(self):
		print('hi')

d = Dog()
d.make_sound()
c = Cat()
c.make_sound()
p = Person()
p.make_sound()