def check_divide(func):
	def inner(a, b):
		if b == 0:
			return 0
		return func(a, b)
	return inner


@check_divide
def divide(a, b):
	return a / b


a = float(input('plz input the molecular: '))
b = float(input('plz input the denominator: '))
r = divide(a, b)
print(r)