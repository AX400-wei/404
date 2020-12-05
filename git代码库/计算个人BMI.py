class BMI:                              #定义BMI类
    def __init__(self,xm,nl,tz,sg):     #初始化函数
        self.xm = xm
        self.nl = int(nl)
        self.tz = int(tz)               #体重是以kg为单位
        self.sg = float(sg)             #使用浮点数，避免输入带小数点的身高时报错
        
    def print_BMI(self):
        print("{n}的BMI指数是{m}".format(n = self.xm,m = self.tz/(self.sg*self.sg)))
        m = self.tz/(self.sg*self.sg)
        if m < 18.5:
            print("偏瘦")
        elif 18.5 <= m <24:
            print("正常")
        elif 24 <= m <30:
            print("偏胖")
            
xm = input("请输入你的姓名:")        #增加互动
nl = input("请输入你的年龄:")
tz = input("请输入你的体重:")
sg = input("请输入你的身高:")

bmi1 = BMI(xm,nl,tz,sg)              #实例化
bmi1.print_BMI()