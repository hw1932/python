#coding=utf-8
'''
1,类中调用属性和方法时，忘记使用self
2
'''
class Fridge:
    '''

    '''
    def __init__(self,items={}):
        '''
        :param items:字典，冰箱中的食品名及数量
        :return:无
        '''
        if type(items) != type({}):
            raise TypeError('Fridge require a dic but was given a %s'%type(items))
        self.items = items
        return

    def __add__multi(self, food_name,quantity):
        #if not food_name in self.itmes:
        self.itmes[food_name] = self.itmes[food_name] + quantity

    def add_one(self,food_name):
        if type(food_name) != type(''):
            raise TypeError('add_one require a str, but was given a %s' % type(food_name))
            #raise TypeError,'add_one require a str, but was given a %s' % type(food_name)
        else:
            self.__add_multi(food_name,1)
        return True

    def add_many(self,food_dic={}):
        if type(food_dic) != type({}):
            raise TypeError('add_many require a dic but was given a %s'%type(food_dic))

        for food_name in food_dic.keys:
            self.__add__multi(food_name,food_dic[food_name])
        return

    def has(self,food_name,quantity):
        '''
        判断食物是否存在并不小于所需数量
        :param food_name:
        :param quantity:
        :return:
        '''
        return self.has_various({food_name:quantity})

    def has_various(self,foods={}):
        if type(foods) != type({}):
            raise TypeError('has_various require a dic but was given a %s'%type(foods))
        try:
            for food_name in foods.keys():
                if self.items[food_name] < foods[food_name]:
                    return False
            return True
        except KeyError:
            return False

    def __get_multi(self,food_name,quantity):
        '''
        取出食物
        :param food_name:
        :param quantity:
        :return:
        '''
        try:
            if (self.items[food_name] is None):
                return False
            if (quantity > items[food_name]):
                return False
            self.items[food_name]=self.items[food_name]-quantity
        except KeyError:
            return False
        return quantity

    def get_one(self,food_name):
        if type(food_name) != type(''):
            raise TypeError('get_one require a str,but given a %s'%type(food_name))
        else:
            return __get_multi(food_name,1)

    def get_many(self,foods={}):
        if self.has_various(foods):
            foods_remove = {}
            for food_name in foods.keys():
                foods_remove[food_name] = self.__get_multi(food_name,foods[food_name])
            return foods_remove

#f = Fridge({'eggs':6,'milk':4,'cheese':3})
#if f.has('cheese',2):
#    print('you 2 ge cheeses')

class Omelet:
    '''
    this class creates an omelet boject.
    '''
    def __init__(self,recipe=[],kind = 'cheese'):
        '''
        这个方法把蛋卷类初始化成奶酪蛋卷
        :param kind:
        :return:
        '''
        self.recipe = recipe
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
        '''
        返回蛋卷种类kind，kind在set_kind方法中作为参数已给self
        :return:
        '''
        return self.kind

    def set_kind(self,kind):
        '''
        传递kind参数给__know_kinds方法并调用，返回成分（材料）字典
        :param kind:
        :return:
        '''
        possible_ingredients = self.__know_kinds(kind)
        if possible_ingredients == False:
            return False
        else:
            self.kind = kind
            self.need_ingredients = possible_ingredients

    def set_new_kind(self,name,ingredients):
        '''
        重新给出煎蛋卷名称和成分字典
        :param name:
        :param ingredients:
        :return:
        '''
        '''
        self.kind = name
        self.need_ingredients = ingredients
        return
        '''
        self.recipe.create(name,ingredients)
        self.set_kind(name)
        return

    def __know_kinds(self,kind):
        '''
        根据kind参数返回对应的字典
        :param kind:
        :return:
        '''
        '''
        if kind == 'cheese':
            return {'eggs':2,'milk':1,'cheese':1}
        elif kind == 'mushroom':
            return {'eggs':2,'milk':1,'cheese':1,'mushroom':2}
        elif kind == 'onion':
            return {'eggs':2,'milk':1,'cheese':1,'onion':1}
        else:
            return False
        '''
        return self.recipe.get(kind)


    def get_ingredients(self,fridge):
        '''
        从冰箱中取出的成分字典赋给from_fridge
        :param fridge:
        :return:
        '''
        self.from_fridge = fridge._ingredients_(self)

    def mix(self,news = True):
        if news == True:
            for ingredient in self.from_fridge.keys():
                print('Mixing %d %s for the %s omelet'%self.from_fridge[ingredient],ingredient,self.kind)
        self.mixed = True

    def make(self):
        if self.mixed == True:
            print('Cooking the %s omelet!'%self.kind)
        self.cooked = True

 #   def quick_cook(self,kind,num,which_fridge):

o = Omelet('cheese')
print('%s' %o.__doc__)
print('%s' %o.__init__.__doc__)
