s={2,3,"1","love","I","wangxiaojing"}
print(s)

if "love" in s:
    print("yes")

if "haha" not in s:
    print("no")

s={2,3,"1","love","I","wangxiaojing"}
for i in s:
    print(i,end=" ")

print("--"*20)
#如下集合里面不能嵌套集合，否则会出错提示 set 不是可哈希类型(unhashable type)
#s={{1,2,3},{"I","love","wangxiaojing"},{4,5,6}}
s={(1,2,3),("I","love","wangxiaojing"),(4,5,6)}
for k,m,n in s:
    print(k,"--",m,"--",n)

for k in s:
    print(k)


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



 #len,max,min:和其它基本函数一致
s={43,23,56,223,4,2,1222,4,323,1}
print(len(s))
print(max(s))
print(min(s))

#set 生成一个集合
L=[1,2,3,4,5]
s=set(L)
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


s={1,2,3,4}
s.remove(4)
print(s)
s.discard(1)
print(s)

s.discard(1100)
print(s)

#remove 不存在的值会报 keyerror（是哈希数据，百度了解）
#remove 和 discard 的区别（百度了解）
#s.remove(1100)
#print(s)


#pop 随机移除一个元素
s={1,2,3,4,5,6,7}
d=s.pop()
print(d)
print(s)