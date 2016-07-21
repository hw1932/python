#coding=utf-8
import random as r
class Fish:
	def __init__(self):
		self.x = r.randint(0,10)
		self.y = r.randint(0,10)
	def move(self):
		self.x -= 1
		print('我的位置是：',self.x, self.y)

class Goldfish(Fish):
	pass

class Carp(Fish):
	pass

class Salmon(Fish):
	pass
	
class Shark(Fish):
	def __init__(self):
            Fish.__init__(self)
            self.hungry = True

	def eat(self):
		if self.hungry:
			print('我饿了,我要吃！')
			self.hungry = False
		else:
			print('吃饱啦')
			self.hungry = True

if __name__ == '__main__':
    #fish = Fish()
    #fish.move()
    shark = Shark()
    Fish.__init__(shark)
    shark.move()
