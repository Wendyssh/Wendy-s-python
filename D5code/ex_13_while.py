#while
#年利率6.7%，本例是每年翻滚，则多少年后本钱多少会翻倍

benqian = 10000
year = 0#存放需要翻本的年数

while benqian <20000:
	benqian=benqian*(1+0.067)
	year += 1

print(year)

# 年利率案例2
#本案例中循环体没有被执行，因为11年的时候已经大于2万了，所以不符合条件，因此没执行。year加1之后才会执行while循环。
while benqian <20000:
	benqian=benqian*(1+0.067)
	year += 1
else:
    print(year)