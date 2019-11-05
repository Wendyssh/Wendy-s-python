#只使用一种 dic 函数即可，不必太过复杂，如下了解即可
#d ={"one":1,"two":2,"three":3}
#print(d)


d=dict([("one",1),("two",2),("three",3)])
print(d)

#访问数据
d={"one":1,"two":2,"three":3}
#注意访问格式，中括号内是键值
print(d["one"])

d["one"]='eins'
print(d)

#成员检测 in not in
#检测的只是 key 内容

d={"one":1,"two":2,"three":3}

if 2 in d:
	print("value")

if "two" in d:
	print("key")

if ("two",2) in d:
	print("kv")

#使用遍历在python 2 和Python3 中区别较大，代码不通用
#按key来使用 for 循环
d={"one":1,"two":2,"three":3}
#使用for循环直接按key 值访问
for k in d:
	print(k,d[k])

#上述代码可改成：
for k in d.keys():
	print(k,d[k])

# 只访问字典的值
for v in d.values():
	print(v)

#注意以下特殊用法 即 d.iterms()
for k,v in d.items():
	print(k,"--",v)
	