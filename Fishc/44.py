#coding:utf-8
import time as t

class MyTimer():
    '''
    self.status表示计时状态标志，0未开始，1开始，2结束
    self.begin开始计时的时间，self.end计时结束的时间，self.t表示end-begin
    '''
    def __init__(self):
        self.status = 0
        self.t = 0
        self.begin = 0  #159 9389 8892
        self.end = 0
    def __str__(self):#print(t)的结果
        if self.status == 0:
            print ('未开始计时')
        elif self.status == 1:
             '计时中...'
        elif self.status == 2:
            print( '总共运行了%s秒' %self.t)
    def __repr__(self):#直接输出t的结果
        if self.status == 0:
            return '未开始计时'
        elif self.status == 1:
            return '计时中...'
        elif self.status == 2:
            return '总共运行了%s秒' %self.t
    #开始计时
    def start(self):
        if self.status == 0:
            self.status = 1
            print('计时开始...')
            self.begin = t.localtime().tm_sec
        elif self.status == 1:
            print('请先调用stop()停止计时')
    #停止计时
    def stop(self):
        if self.status == 0:
            print('请先调用start()开始计时！')
        elif self.status == 1:
            self.end = t.localtime().tm_sec
            self.t = self.end - self.begin
            print('成功调用stop()方法，计时结束')
            #改变计时器状态
            self.status = 2
            #为下一轮计时初始化变量
            self.begin = 0
            self.end = 0
        elif self.status == 2:
            print('请先调用start()方法开始计时')
    def __add__(self, other):
        return int.__add__(self.t, other.t)

class Mytimer2():
    '''
    定义了一个计时器，并有add方法，可以把2次计时结果相加
    '''
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.unit = ['年','月','日','时','分','秒']
        self.lasted = []
        self.prompt = '未开始计时'
    def __str__(self):
        return self.prompt
    __repr__ = __str__
    def __add__(self, other):
        add_last = []#两次时间之和存储在这个空列表中
        prompt = '2次总共运行了'
        for index in range(6):
            add_last.append(self.lasted[index] + other.lasted[index])
            if add_last[index]:
                prompt += (str(add_last[index]) + self.unit[index])
        print(prompt)
    def start(self):
        if not self.begin:
            self.begin = t.localtime()
            self.prompt = '计时中，请先调用stop()停止计时'
            print('开始计时')
        elif self.begin:
            print('请先调用stop()停止计时')
    def stop(self):
        if self.begin:
            self.end = t.localtime()
            self.__calc2()
            print('计时结束')
            #为下一轮计时初始化变量
            self.begin = 0
            self.end = 0
        elif not self.begin:
            print('请先调用start()进行计时')
    def __calc(self):
        self.prompt = '总共运行了'
        self.lasted = []
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
    def __calc2(self):#__calc中begin-end方法可能是负，下面是完善
        self.prompt = '总共运行了'
        self.lasted = []
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index] < 0:
                if index == 1:#月为负时
                    self.lasted[index-1] = self.lasted[index-1] - 1#年减1
                    self.lasted[index] += 12#月加12
                elif index == 2:#日为负时
                    self.lasted[index-1] -= 1#月减1
                    self.lasted[index] += 30#日加30，不再区分某个月，太繁琐
                elif index == 3:#小时为负时
                    self.lasted[index-1] -= 1#日减1
                    self.lasted[index] += 24#小时加24
                elif index == 4:#分为负时
                    self.lasted[index-1] -= 1#小时减1
                    self.lasted[index] += 60#分加60
                elif index == 5:#小时为负时
                    self.lasted[index-1] -= 1#分减1
                    self.lasted[index] += 60#秒加60
                self.prompt += (str(self.lasted[index]) + self.unit[index])
            elif self.lasted[index]>0:
                self.prompt += (str(self.lasted[index]) + self.unit[index])