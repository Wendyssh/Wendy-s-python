#5+4j 中的j 如果换成其它字母如m和k等则提示语法错误，为什么？
L=['a','I love China',45, 760,(5+4j)]
print(L)

#append 插入一个内容，在末尾追加
a =[i for i in range (1,5)]
print(a)
a.append(100)
print(a)


#insert(index,data),插入位置是 index 的前面
print(a)
a.insert(3,666)
print(a)

#del
print(a)
del a[0]
print(a)

#pop
print(a)
last_ele = a.pop()
print(last_ele)
print(a)


#remove
print(a)
print(id(a))
a.remove(666)
print(a)
print(id(a))
#输出的两个id值一样，说明remove操作是在员list上直接操作

#clear
a = [1,2,3,4,5]
print(a)
print(id(a))

a.reverse()
print(a)
print(id(a))


print(a)
a.append(8)
a.insert(4,8)
print(a)
a_len=a.count(8)
print(a_len)

#列表类型变量赋值示例
a =[1,2,3,4,5,666]
#list类型，简单赋值操作，是传地址
b=a
b[3]=777
print(a)
print(b)

print("*"*20)
#为解决这个问题，复制的时候需要拷贝
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))
print("*"*30)
b[3]=888
print(a)
print(b)

print("*"*40)
a = [1,2,3,[10,20,30]]
b = a.copy()
print(id(a))
print(id(b))
print(id(a[3]))
print(id(b[3]))
a[3][2]=666
print(a)
print(b)