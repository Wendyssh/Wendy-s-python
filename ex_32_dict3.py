#字典生成式
d={"one":1,"two":2,"three":3}

#常规字典生成式
dd = {k:v for k,v in d.items()}
print(dd)

#加限制条件的字典生成式
dd = {k:v for k,v in d.items() if v%2==0}
print(dd)

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

#keys:访问字典的键组成的一个结构(可迭代结构)
k=d.keys()
print(type(k))
print(k)

#values:同理，一个可迭代的结构
v=d.values()
print(type(v))
print(v)

#get:根据指定键返回相应的值，好处是可以设置默认值
d={"one":1,"two":2,"three":3}
#get 默认值是None，可以设置
print(d.get("on333"))
#体会上下的区别:下面提示keyerror，但上面的会返回默认值 None
#print(d["on333"])
print(d.get("one",100))
print(d.get("on333",100))

#fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有键的值
L=["one","two","three"]
#注意fromkeys两个参数的类型
#注意fromkeys的调用主体
d=dict.fromkeys(L,"hahhahaha")
print(d)