i = 0
err_count = 0
while True:
	try:
		s = input('enter a number: ')
		n = int(s)
		print(f'good, you entered {n}')
	except ValueError:
		err_count += 1
		if err_count >= 3:
			print('you only have 3 chance to fail!!!!!!')
			break
	except KeyboardInterrupt:
		print('game over!!!!!')
		break
	finally:
		i += 1
		print(f'this is your {i} try!')