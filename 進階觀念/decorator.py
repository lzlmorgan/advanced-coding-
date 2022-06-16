#裝飾器 decorator
import time

def print_func(func):
	def inner():
		print('running', func.__name__)
		func()
	return inner   #跑func名字


def time_func(func):
	def inner():
		start = time.time()
		func()
		end = time.time()
		print('elapsed', end - start, 'secs')
	return inner   #跑時間差

def test():
	print('hi')

def test2():
	print('hello')


print('--------in processing--------')
test = print_func(test)
test2 = print_func(test2)
test()
test2()

print('---------in processing--------')
test = time_func(test)
test2 = time_func(test2)
test()
test2()