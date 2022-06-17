#property
#encapsulation封裝. oop物件導向變成 把class的內部細節隱藏讓別人無法觸及

class Batman:
	def __init__(self, hp):
		self._hp = hp

	#getter method	
	def get_hp(self):
		return self._hp 

	#setter method
	def set_hp(self, hp):
		self._hp = hp