110413301400 Tuple
元组 Tuple
元组可以看做是一个不可更改的 list，不可“写”操作。
1、元组创建
案例
#创建空元祖
t=()
print(type(t))

#创建一个只有一个值的元组，也可不加括号写成 t=1, 结果一样
t=(1,)
print(type(t))
print(t)

t=1,
print(type(t))
print(t)


#如果没有逗号的话，会被判断为整数
t=(1)
print(type(t))
print(t)


#创建多值元组
t=(1,2,3,4,5)
print(type(t))
print(t)



t=1,2,3,4,5
print(type(t))
print(t)

#使用其它结构创建
L=[1,2,3,4,5]
print(type(t))
print(t)


2、元组的特性
（1）有序列表，有序
（2）元组数据值可以访问，不能修改！！！
（3）元组数据可以是任意类型
（4）总之，list 所有特性，除了可修改外，元组都具有
（5）也就意味着，list具有的一些操作如索引、分片、序列想加、相乘、成员资格操作等一模一样
#创建空元祖
t=()
print(type(t))

#创建一个只有一个值的元组，也可不加括号写成 t=1, 结果一样
t=(1,)
print(type(t))
print(t)

t=1,
print(type(t))
print(t)


#如果没有逗号的话，会被判断为整数
t=(1)
print(type(t))
print(t)


#创建多值元组
t=(1,2,3,4,5)
print(type(t))
print(t)



t=1,2,3,4,5
print(type(t))
print(t)

#使用其它结构创建
L=[1,2,3,4,5]
print(type(t))
print(t)


#索引操作
t=(1,2,3,4,5)
print(t[4])

#超标错误
#print(t[12])

t=(1,2,3,4,5,6)
t1=t[1::2]
print(id(t))
print(id(t1))
print(t1)
#切片可以超标
t2=t[2:100]
print(t2)

#序列相加
t1=(1,2,3)
t2=(5,6,7)

#传址操作
print(t1)
print(id(t1))

t1+=t2
print(id(t1))

#以上操作，类似于
t1=(1,2,3)
t2=(2,3,4)

#tuple 的不可修改，指的是内容的不可修改
#修改tuple内容会导致报错
#t1[1]=100

#元组相乘
t=(1,2,3)
t=t*3
print(t)

#成员检测
t=(1,2,3)
if 2 in t:
	print("YEs")
else:
	print("No")

#元组遍历，一般采用 for
#1、单层元组遍历
t=(1,2,3,"wangxiaojing","1","love")
for i in t:
	print(i,end = " ")

#2、双层元组遍历
t=((1,2,3),(2,3,4),("i","love","wangxiaojing"))
#对以上孕足的遍历，可以如下

for i in t:
	print(i)

for k,m,n in t:
	print(k,'--',m,'--',n)