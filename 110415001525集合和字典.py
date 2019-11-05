20191104142015001525:集合和字典
1、集合 set
(1)高中数学概念
（2）已对确定的无序的唯一的数据，集合中每一个数据成为一个元素

案例 ex_32_setdic.py
#集合的定义
s=set()
print(type(s))
print(s)

#如果只是用大括号定义，则定义的是一个字典类型
d={}
print(type(d))
print(d)

#此时大括号内一定要有值，否则定义的是一个字典dict

s={1,2,3,4,5,6,7}
print(s)


3、集合的特征
(1)集合内的数据无序，既无法使用索引和分片
（2）集合内部数据元素具有唯一性，可以用来排除重复数据
（3）集合内的数据 str,int,float,tuple,冰冻集合等，即内部职能放置可哈希数据（百度了解可哈希和不可哈希数据）

4、集合序列操作
#成员检测
#in,not in
案例 ex_32_setsdic.py
s={2,3,"1","love","I","wangxiaojing"}
print(s)

if "love" in s:
    print("yes")

if "haha" not in s:
    print("no")

5、集合遍历操作

#for 循环
s={2,3,"1","love","I","wangxiaojing"}
for i in s:
    print(i,end=" ")

#带有元组的集合遍历
 s={(2,3,4),("1","love","wangxiaojing"),(3,4,5)}
 for k,m,n in s:
     print(k,"--",m,"--",n)

 for k in s:
     print(k)


6、集合的内涵
#普通集合内涵
s={23,223,545,3,1,2,3,4,3,2,3,1,2,4,3}
#以下结合在初始化后自动过滤掉重复元素
print(s)

#普通吉和内涵
ss={i for i in s}
print(ss)

#带条件的集合内涵
sss ={i for i in s if i%2 == 0}
print(sss)

#多循环的集合内涵
s1={1,2,3,4}
s2={"i","love","wangxiaojing"}

s={m*n for m in s2 for n in s1}
print(s)
print("*"*40)
s={m*n for m in s2 for n in s1 if n ==2}
print(s)


7、集合函数/关于集合的函数
 #len,max,min:和其它基本函数一致
s={43,23,56,223,4,2,1222,4,323,1}
 print(len(s))
 print(max(s))
 print(min(s))

#set 生成一个集合
L=[1,2,3,4,5]
s=set{L}
print(s)

#add：向集合内添加元素
 s={1}
 s.add(222222)
 print(s)

 #clear
 s={1,2,3,4}
 print(id(s))
 s.clear()
 print(id(s))
 #结果表明clear 函数是原地清除数据

#copy：拷贝
#remove: 移除指定的值
#discard:移除集合中指定的值

s={1,2,3,4}
s.remove(4)
print(s)
s.discard(1)
print(s)

s.discard(1100)
print(s)

#remove 不存在的值会报 keyerror（是哈希数据，百度了解）
#s.remove(1100)
#print(s)


#集合函数
#intersection:交集
#difference:差集
#Union:并集
#issubset：检查一个集合是否为另一个子集
issuperset:检查一个集合是否为另一个超集

s1={1,2,3,4,5,6}
s2={5,6,7,8,9}

s_1 = s1.intersection(s2)
print(s_1)

s_2=s1.difference(s2)
print(s_2)

s_3=s1.issubset(s2)
print(s_3)


#集合的数字操作
s1={1,2,3,4,5,6}
s2={5,6,7,8,9}
s_1=s1-s2
print(s_1)

#不支持加法 s_2=s1+s2
#print(s_2)

8、frozen set:冰冻结合
即不可以进行任何操作的结合
它是一种特殊集合
#创建
s=frozenset()
print(type(s))
print(s)


二、dict字典
1、字典是一种组合数据，没有顺序的组合数据，数据以键值对的形式出现

#字典的创建
#空值
d={}
print(d)

d=dict()
print(d)

#创建有值的字典，每一组数据用冒号隔开，每一对键值对用逗号隔开
d={"one":1,"two":2,"three":3}
print(d)

#创建有内容的字典1:一个字典值的参数
d=({"one":1,"two":2,"three":3})
print(d)


#用dict 创建有内容字典2：多个关键字参数
#利用关键字参数
#d=("one"=1,"two"=2,"three"=3)
#print(d)

