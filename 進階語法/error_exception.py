s = input('enter a number: ')

try:
	n = int(s)
except ValueError: #捕捉所有的錯誤
	print('ValueError caught!!')
