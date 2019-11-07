#break
#在一个队列中，寻找数字7，如找到打印出来即可且结束
dig_list=[1,2,3,4,5,6,7]
for dig in dig_list:
	#原来写成 if dig_list == 7，运行结果和预期不同
	if dig ==7:
		print("终于找到了")
		break
	else:
		print(dig)


#continue
#在数字1-10中，寻找所有偶数，找到后打印
dig_list=[1,2,3,4,5,6,7,8]
'''
continue
'''
for dig in dig_list:
	if dig%2==0:
		print(dig)
		print("haha,ifoundit.")
	else:
		continue

#此段代码和上面一样
print("*"*30)
for dig in dig_list:
	if dig%2==1:
		continue
	print(dig)
	print("haha,ifoundit.")
	
#pass1
age = 19
if age>19:
	pass
else:
	print("你还小")

#pass后如果有其它命令，继续执行，并非简单跳过
dig_list=[1,2,3,4,5,6]
for dig in dig_list:
	if dig%2==0:
		pass
		print(dig,"双数")