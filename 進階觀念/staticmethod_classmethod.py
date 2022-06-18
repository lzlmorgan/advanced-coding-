#staticmethod & classmethod 不建議實例instance可以使用class的def

class Batman:
	def __init__(self, hp):
		self.hp = hp

	@staticmethod
	def f(): #不需要self, 不用創建instance就可以使用
		print('static method')

	@staticmethod
	def calc_avg(x):
		return sum(x) / len(x)

	@classmethod	
	def fffff(cls): #cls=classmethod cls彷彿建議一個instance接受數據
		cls(hp).f() #instance hp=100

#測試classmethod 需要運勢實例
hp = 100
Batman.fffff()
print('------------------')
#測試staticmethod 不需要建議實例
x = [1, 2, 3,11]
print(Batman.calc_avg(x))
