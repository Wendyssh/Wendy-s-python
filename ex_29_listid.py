#id函数距离
a =100
b =200
print (id(a))
print (id(b))

c=a
print (id(c))

#a和c并非同一份数据
a =101
print (a)
print (c)

#通过 id 可直接判断数据是否相同
L=[1,2,3,4,5]
LL = L[:]
LLL = LL

print (id(L))
print (id(LL))
print (id(LLL))

#通过 id 知道，LL 和 LLL 是一份数据，验证代码如下：(不太理解)

L[1] = 100
print(L)
print (LL)

LL[1]=100
print(LL)
print(LLL)