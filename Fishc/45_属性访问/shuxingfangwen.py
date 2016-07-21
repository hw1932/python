
class C1:
    def __init__(self):
        self.x = 'x-man'
    def p(self):
        print('this is p func')
        return

def C1_func():
    cc = C1()
    print(getattr(cc,'x','not found'))
    C1().p()

class C2:
    def __init__(self,size=20):
        print('__init__')
        self.size = size

    def getSize(self):
        return  self.size

    def setSize(self,value):
        self.size = value

    def delSize(self):
        del self.size

    x = property(getSize,setSize,delSize)

class C2:
    # def __init__(self,size=20):
    #     print('__init__')
    #     self.size = size
    def __getattr__(self, name):
        print('getattr')
    def __getattribute__(self, name):
        print('getattribute')
        return super().__getattribute__(name)
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key, value)
    def __delattr__(self, name):
        print('delattr')
        super().__delattr__(name)

class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            #self.__init__(self,width=value,height=value)
            self.width = value
            self.height = value
        else:

            super().__setattr__(key,value)
    x = property(fset=setattr)

    def getArea(self):
        return self.width*self.height

if __name__ == '__main__':
    # print('61')
    # c2 = C2()
    # print(63)
    # c2.x = 1
    # print(65)

    # print('----------')
    # c2.x
    # print('---')
    # del c2.x
    # c2.x

    r1 = Rectangle(5,4)
    #print(r1.getArea())
    r1.square = 10
    print(r1.width,r1.height)
