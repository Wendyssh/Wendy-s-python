#MOOCstr_week.py
weekStr =("星期一星期二星期三星期四星期五星期六星期日")
weekId = eval(input("请输入星期数字 (1-7):"))
pos = (weekId-1)*3
print(weekStr[pos:pos+3])

#后面的不包含如星期二中的“二”处于的位置是第5位，那么在切片中终止索引的位置是6

