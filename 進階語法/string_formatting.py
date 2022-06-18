#string_formatting

#最原始的string format
name = 'Allen'
x = 10
y = 3.14
print('hi %s' % name) #s = string 
print('hi %d' % x) #d = data
print('hi %f' % y) #f = float
print('hi %s, my number is %d' % (name, x)) #一個或以上的組合

print('---------------------')
#string format第二種模式
print('hi {}, my num is {}'.format(name,x))

print('--------------------')
#最新的f string python3.6+
print(f'hi{name}, my num is {x}')

