#scope 範圍
#LEGB rule 取值顺序
#L: local 低
#E: enclosed
#G: global
#B: built_in 高
#底层对高层只能读取不能写入

x = 1
def f():
	global x
	x = 10

f()
print(x) 