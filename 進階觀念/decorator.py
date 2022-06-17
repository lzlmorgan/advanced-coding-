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

@time_func
@print_func
def test():
	for i in range(10000000):
		i = i + 1
	print(i)

@time_func
@print_func
def test2():
	print('hello')


test()
print('-------------------------------')
test2()

