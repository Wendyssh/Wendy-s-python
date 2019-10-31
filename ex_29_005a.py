x = 100
y = 200

z1 = x+y
#1. 注意字符串中引号的写法
#2.比对 exec执行结果和代码执行结果
z2 = exec("print('x+y: ', x+y)")
#打印结果为 300 None
print(z1)
print(z2)