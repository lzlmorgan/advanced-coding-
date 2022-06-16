#裝飾器 decorator

def print_func(func):
	def inner():
		print('running', func.__name__)
		func()
	return inner

def test():
	print('hi')

def test2():
	print('hello')


print('in processing')
test = print_func(test)
test2 = print_func(test2)
test()
test2()