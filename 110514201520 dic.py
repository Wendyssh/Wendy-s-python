110514201520 dic

#只使用一种 dic 函数即可，不必太过复杂，如下了解即可
#d ={"one":1,"two":2,"three":3}
#print(d)


d=dict([("one",1),("two",2),("three",3)])
print(d)

#如下案例不可运行
#d=(one=1,two=2,three=3)
#print(d)


一、字典的特征
（1）字典是序列类型但是无序序列，所以没有分片和索引
（2）字典中的数据每个都有键值对组成，即kv对。
（3）key：必须是可哈希的值如 int,string,float,tuple但 list,set,dict 不行
     value: 任何值

二、字典常见操作
案例 ex_32_dic2.py
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
	
二、字典生成式：
案例 ex_32_dict3.py
#字典生成式
d={"one":1,"two":2,"three":3}

#常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)

#加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v%2==0}
print(dd)



三、字典相关函数
#通用函数：len,max,min,dict
#str(字典)：返回字典的字符串格式

d={"one":1,"two":2,"three":3}
print(str(d))

#clear:清空字典
#items:返回字典的键值对组成的元组格式
d={"one":1,"two":2,"three":3}
i=d.items()
print(type(i))
print(i)
