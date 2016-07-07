#coding=utf-8
class Omelet:

    def __init__(self,kind = 'cheese'):
        '''
        这个方法把蛋卷类初始化成奶酪蛋卷
        :param kind:
        :return:
        '''
        self.set_kind(kind)
        return

    def _ingredients_(self):
        '''
        internal method to be called on by a fridge
        or other objects that need to act on ingredients
        内部方法被称为一个冰箱或其他对象，需要采取行动的成分
        :return:
        '''
        return  self.needed_ingredients

    def get_kind(self):
        return self.kind

    def set_kind(self,kind):
        possible_ingredients = self.__know_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.need_ingredients = possible_ingredients

    def set_new_kind(self,name,ingredients):
        self.kind = name
        self.need_ingredients = ingredients
        return

    def _know_kinds(self,kind):
        if kind == 'cheese':
            return {'eggs':2,'milk':1,'cheese':1}
        elif kind == 'mushroom':
            return {'eggs':2,'milk':1,'cheese':1,'mushroom':2}
        elif kind == 'onion':
            return {'eggs':2,'milk':1,'cheese':1,'onion':1}
        else:
            return False

    def get_ingredients(self,fridge):
        self.from_fridge = fridge._ingredients_(self)

    def mix(self):
        for ingredient in self.from_fridge.keys():
            print('Mixing %d %s for the %s omelet'%(self.from_fridge[ingredient],ingredient,self.kind))
        self.mixed = True

    def make(self):
            if self.mixed == True:
                print('Cooking the %s omelet!'%self.kind)
                self.cooked = True