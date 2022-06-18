#generator  产生器iterator
#通过yeild来实现 节约记忆体的存储位置

def g():
	while True:
		yield 1

print(next(g()))



def my_range(n):
	i = 0
	while i < n:
		print(f'start to print{i}')
		yield i
		i += 1

for i in my_range(20):
	print(i)

print(my_range(5)) #生成iterator


print('----------------------')
#list comprehension
x = [0, 1, 2, 3, 4]
print([i*i for i in x]) #[]正常list
print((i*i for i in x)) #()生成iterator
it1 = (i*i for i in x)
it2 = (i+1 for i in it1)
print(next(it2))
print(next(it2))

# print(next(it))
# print(next(it))
# print(next(it)) #......

