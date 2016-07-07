class Fridge:
    '''

    '''
    def test(self):
        print('success')
    def display(self):
        print('this class Fridge has a def named display')
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