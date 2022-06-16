# _ 不重要不需要体现的object, 或者临时的object
# _name ->public(公共使用)/private(私人使用). 前底线表示private,没有实际功能 
# _ 一个底线improt*时不会被import
# name_ 名字后_表示已经使用过的名称

# __name 名字前双底线,避免撞名字
# __name__ python预留的初始化function, dunder methods/magic methods

for _ in range(10):
	print('hi') 

#----------------------------
class Qwe:
	def public_function(self):
		print('asdasd')
		self._convert_date()

	#helper function
	def  _private_function(self):
		print('asdasas')

	def _convert_date():

q = Qwe()
q.public_function()
q._private_function()


#---------------------------



