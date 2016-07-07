#coding=utf-8
#from Kitchen import *
import os
import test11
from test11 import test_2
#import .Kitchen
#r = Kitchen.fridge.Fridge()
#test_2().test_print()

import Kitchen

Kitchen.Foods.Recipe().display()
#from Kitchen.Foods import Recipe

#Recipe().display()
#print(os.getcwd())

"""
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
'''
f = Fridge({'eggs':6,'milk':4,'cheese':3})
if f.has('cheese',2):
    print('you 2 ge cheeses')
'''
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

class Recipe:
    def __init__(self):
        self.set_default_recipes()
        return
    def set_default_recipes(self):
        self.recipes = {'cheese':{'eggs':1,'milk':1,'cheese':1},'mushroom':{'eggs':2,'milk':1,'cheese':1,'mushroom':2},'onion':{'eggs':2,'milk':1,'cheese':1,'onion':1}}
    def get(self,name):
        try:
            recipe = self.recipes[name]
            return recipe
        except KeyError:
            return False

    def create(self,name,ingredients={}):
        self.recipes[name] = ingredients

    def display(self):
        print ('this class Recipe has a def named display')
"""