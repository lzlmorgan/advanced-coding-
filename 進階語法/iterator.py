#iterator 迭代器

x = [1, 2, 3]
print(dir(x)) #print出x能使用的class, __iter__
print('--------------------------')
it = iter(x) #it = x.__iter__() print出__iter__能使用的类---__next__用来取值
print(dir(it))
print(it.__next__()) #去list x第一个值 1
print(it.__next__()) #去list x第一个值 2
print(it.__next__()) #去list x第一个值 3
print(it.__next__()) #stopiteration

print(sum(it))
print(sum(it)) #iterator只能按顺序取一次.



