#closure 闭包
#lifecycle


def f():
	x = 1 #enclose
	def inner():
		print(x) #local
	return inner

y = f()
print(y) #显示结果为<function f.<locals>.inner at 0x10276e710>
y()
