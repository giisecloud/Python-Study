#记录生肖，根据年份来判断生肖
#记录星座，根据月日来判断星座

#输入出生年月日
inputyear = input("请输入你的出生年份：")
inputmonth = input("请输入你的出生月份： ")
inputday = input("请输入你的出生日期： ")
#生肖变量及数据类型转换
chinese_zodia = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
year = int (inputyear)

#星座变量及数据类型转换
constellation_name = (u'摩羯座', u'水瓶座', u'双鱼座' , u'白羊1', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座',
                 u'天秤座', u'天蝎座', u'射手座' )
constellation_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))

(month,day) = int (inputmonth),int (inputday)

constellation_day = filter(lambda  x: x<= (month,day) , constellation_days)

constellation_len = len(list(constellation_day)) % 12
#输出生肖，星座
print ("你的生肖属: ",chinese_zodia[year % 12])
print("你的星座是: ",constellation_name[constellation_len])





