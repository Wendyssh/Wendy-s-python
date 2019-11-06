#考试成绩判断
score=input("请输入您的成绩： ")
try:
	float(score)
	print()
except:
	print("请重新输入。")
if score >=90:
	print("优秀")
elif score >=80:
    print("良")
elif score>=70:
	print("中")
elif score>=60:
	print("平")
else:
	print("要努力啊")