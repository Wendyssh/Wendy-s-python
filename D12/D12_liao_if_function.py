#廖雪峰-条件判断 https://www.liaoxuefeng.com/wiki/1016959663602400/1017099478626848
#练习题

H = 1.75
W = 80.5
BMI = W/H**2
if BMI < 18.5:
    print("过轻")
elif 18.5<BMI<25:
    print("正常")
elif 25<BMI<28:
    print("过重")
elif 28<BMI<32:
    print("肥胖")
else:
    print("严重肥胖")