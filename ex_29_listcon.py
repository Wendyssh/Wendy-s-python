#列表加号
a = [1,2,3,4]
b = [5,6,7,8]
d = [9,10,22,33]

c = a+b+d
print (c)

#列表相乘，相当于把n个列表拼接在一起

a = [1,2,3,4]
b = a*3
print (b)

#成员资格运算
# 判断元素是否在List里面

a = [1,2,3,4,5]
b = 8
c = b in a
print (c)

b = 4
c = b in a
#print (b in c)布尔值不可迭代，是错的，要改成如下
print (b in a)

#not in
a = [1,2,3,4,5]
b = 9

print(b not in a)


