#closure 闭包

def f():
	x = 1
	def inner():
		print(x)
	return inner

y = f()
print(y) #显示结果为<function f.<locals>.inner at 0x10276e710>
