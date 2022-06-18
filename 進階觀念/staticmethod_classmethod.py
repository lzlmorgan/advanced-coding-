#staticmethod & classmethod 讓程序員不需要實例就可以使用

class Batman:
	def __init__(self, hp):
		self.hp = hp

	@staticmethod
	def f(): #不需要self, 不用創建instance就可以使用
		print('static method')

	@staticmethod
	def calc_avg(x):
		return sum(x) / len(x)

x = [1, 2, 3,11]
print(Batman.calc_avg(x))

