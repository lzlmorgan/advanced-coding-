#property
#encapsulation封裝. oop物件導向變成 把class的內部細節隱藏讓別人無法觸及

class Batman:
	def __init__(self, hp):
		self.hp = hp

b1 = Batman(100)
b2 = Batman(200)
b1.hp = b1.hp + b2.hp
