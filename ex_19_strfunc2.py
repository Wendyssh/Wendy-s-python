#isalpha：以下三个都不是字母，因为其中含有空格等。第四个是
s1 = "你好，世界"
s2 = "Hello, world"
s3 = "waelfjklewajkl is."
s4 = "ldjaljfdlakjlkdjfa"

print (s1.isalpha())
print (s2.isalpha())
print (s3.isalpha())
print (s4.isalpha())

#判断是否是数字，罗马数字可能有问题
chin_num = "一二三四"
print(chin_num.isdigit())
print(chin_num.isnumeric())
print(chin_num.isdecimal())

#内容判断类
dana = "Liu Dana"
xiaojing = "Xiao jing"
s="Liu Dana really loves wang Xiao jing"
print(s.startswith(dana))
print(s.endswith(xiaojing))


#islower()  isupper()空格不影响结果
s="Liu Dana really loves wang Xiao jing"
s1="LiuDana really loves wang Xiao jing"
s2="liudanareallyloveswangXiaojing"
#该判断不适用于汉字内容
s4="的框架阿卡丽点就发了就按开始登记福利卡圣诞节"
s5="NNN DLAJFLKAJSD LDKJAFLKJDAL"
s6="Ndkjal Nlkjlkjl NLJLKJL"

print(s.isupper())
print(s1.islower())
print(s2.islower())
print(s4.isupper())
print(s5.isupper())
print(s6.isupper())