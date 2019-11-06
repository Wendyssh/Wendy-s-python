#字符串为空的if结构
a = ""
if a:
	print("dakjdajkl")
print("kdlajkldja")

#字符串不为空
a="kdlajkl"
if a:
	print("yes")

print("twoyes")

#input(自己扩展的 try 和 except 用法，不知是否正确。想要用户输入的只能是确定的几个汉字，不能是字母组合或其它)
gender = input("请输入内容： ")
try:
	if gender=="男" or gender=="女":
		print(gender)
	else:
		print(input("请输入正确内容: "))
except:
	print(gender)
	
