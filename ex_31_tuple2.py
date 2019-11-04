#count:计算指定数据出现的次数
t=(1,2,3,45,1,1,2,)
print(t.count(2))

#index:求指定元素在元组中的索引位置
print(t.index(45))

#如果需要查找的数字是多个，则返回第一个
print(t.index(1))

a=1
b=3

print(a)
print(b)
print("*"*20)
a,b=b,a
print(a)
print(b)