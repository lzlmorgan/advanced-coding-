#property
#encapsulation封裝. oop物件導向變成 把class的內部細節隱藏讓別人無法觸及

class Batman:
	def __init__(self, hp):
		self.hp = hp

	@property #getter method
	def hp(self):
		print('asdasd')
		return self._hp #真正存儲需要運算數據的地方

	@hp.setter
	def hp(self, hp):
			if hp >100:
				self._hp = 100
			elif hp < 0:
				self._hp = 0
			else:
				self._hp = hp 

b1 = Batman(100)
b1.hp = 150 #不用动用b1.hp() 直接调用@property print出结果
print(b1.hp)
# b2 = Batman(200)
# b1.hp = b1.hp + b2.hp
