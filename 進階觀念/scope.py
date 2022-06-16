#scope 範圍
#LEGB rule 取值顺序
#L: local 低
#E: enclosed
#G: global
#B: built_in 高
#底层对高层只能读取不能写入



#顺序
#权限
#global語法
#nonlocal語法
#lifecycle: def(function)運作了,local區域才工作--生命週期
#不建議用同名

x = 1
def f():
	global x  #global可以跨区域取值
	x = 10

f()
print(x)

print('--------------------')
def f():
	x = 1
	def ff():
		  nonlocal x #跨enclosed取local值
		x = 10
	ff()
	print(x)

f()
