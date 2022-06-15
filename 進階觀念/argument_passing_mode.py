#pass by value複製一份
#pass by reference直接把原數值放入
#pass by object reference/pass by sharing 設值指令會隔開sharing 




#example 1
def f(y):
	y.append(1)
x = [0]
f(x)
print(x)

print('-----------')
#example 2
def f(y):
	y = []
x = [0]
f(x)
print(x)

print('------------')
#example 3
def ff(y):
	y += 1

x = 0
ff(x)
print(x)