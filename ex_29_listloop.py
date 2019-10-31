# for in list
a = [1,2,3,4,5]

#挨个打印a里面的元素
for i in a:
    print (i)

b = ['I love Python','I love the world']

for i in b:
	print (i)


#rang
#in 后面的变量要求是可迭代的内容（可迭代内容还没讲到
for i in range(1,10):
	    print (i)
print(type(range(1,10)))

#while 循环访问list
#一般不用while 遍历 list

a=[1,2,3,4,5,6]
length = len(a)

#indx 表示的是 list 的下标
indx = 0
while indx < length:
    print (a[indx])
    indx+=1


#双层列表循环
#a 为嵌套列表或称为双层列表

a = [['one',1],['two',2],['three',3]]

for k,v in a:
    print(k,"--",v)

#双层列表循环变异
# for k,v in a 是特例写法，如果value 太多就会报错 too many value to unpack,如：
# a = [['one',1,"eins"],['two',2],['three',3,4,5,6,7]]
#但可以修改为 a = [['one',1，'eins'],['two',2,'zwei'],['three',3,'drei']]，它是一种变异
a = [['one',1],['two',2],['three',3]]

for k,v in a:
    print(k,"--",v)


a = [['one',1,'eins'],['two',2,'zwei'],['three',3,'drei']]
for k,v,w in a:
    print(k,"--",v,"--",w)


#for 创建
a = ['a','b','c']
#用list a c创建一个list b
#对于所有a 中的元素，逐个放入新列表b 中
b = [i for i in a]
print (b)

#对于a中所有元素乘以10，放入新 list
a = ['a','b','c']
#用list a c创建一个list b
#对于所有a 中的元素，逐个放入新列表b 中
b = [i*10 for i in a]
print (b)

#还可以过滤原来List 中的内容放入新列表
#提取a 中的所有偶数放入b

a = [x for x in range(1,35)]
b = [m for m in a if m % 2== 0]
print (b)

#列表生成式可嵌套
#两个列表a,b
a = [i for i in range(1,4)]
print (a)

b = [i for i in range(100,400) if i % 100 == 0]
print (b)

#列表生成式可以嵌套，此事等于两个 for 循环嵌套
c=[m+n for m in a for n in b]
print (c)

for m in a:
	for n in b:
		print (m+n, end = '')
print()

#嵌套的列表生成式也可以用条件表达式
c= [m+n for n in a for n in b if m+n <250]
print (c)