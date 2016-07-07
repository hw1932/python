#coding=utf-8
class car:
    car_type = ''
    number = 0
    colour = ''
    def __init__(self,ct,n,c):
        self.car_type = ct
        self.number = n
        self.colour = c

    def whistle(self):
        print('%s :嘀嘀嘀~！'%(self.car_type))

    def run(self):
        print('%s %s 用 %d 个轮子奔驰在路上!'
        %(self.colour,self.car_type,self.number))

c = car('轿车',4,'蓝色')
c.whistle()
c.run()