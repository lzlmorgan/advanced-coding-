#closure 闭包
#lifecycle


def f():
	x = 1 #enclose
	def qqq():
		print('asdasda')

	def inner():
		print(x) #local
		qqq()
	return inner #inner 直接封裝了def qqq

y = f()
print(y) #显示结果为<function f.<locals>.inner at 0x10276e710>
y()