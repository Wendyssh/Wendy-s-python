#len 求列表长度
a = [x for x in range (1,100)]
print (len(a))

 #max: 列表中最大值
print(max(a))

#min：最小值
b=['man','file','python']
print(max(b))

#list:将其它格式的数据转换成 list
a = [1,2,3]
print (list(a))

#把所有字符都单列出来，注意空格字符也会打印
s= 'I love China'
print(list(s))

#转换成 range
#被转换的类型必须是可迭代的
print(list(range(12,19)))
