'''
meal - Module for making meals in Python
Import this module and then call
makeBreakfast(),makeDinner() or makLunch().
'''
__all__ = ['Meal','AngryChefException','makeBreakfast','makeLunch','makeDinner','Breakfast','Lunch','Dinner']
#helper functions.
def makeBreakfast():
    '''
    Create a Breakfast object.
    :return:
    '''
    return Breakfast()

def makeLunch():
    '''
    Create a Breakfast objcet.
    :return:
    '''
def makeDinner():
    '''
    Create a Dinner object.
    :return:
    '''
    return Dinner()
class AngryChefException(Exception):
    '''
    Exception that indicates the chef is unhappy.
    '''
    pass
class Meal:
    '''
    Holds the food and drink used in a meal
    In true object-oriented tradition,this class includes setter methods fro the food ank drink.

    call printIt to pretty-print the values.
    '''
    def __init__(self,food='omelet',drink='coffee'):
        '''
        Initialize to default values.
        :param food:
        :param drink:
        :return:
        '''
        self.name = 'generic meal'
        self.food = food
        self.drink = drink

    def printIt(self,prefix=''):
        '''
        print the data nicely.
        :param prefix:
        :return:
        '''
        print(prefix,'A fine',self.name,'with',self.food,'and',self.drink)
    # Setter for the food
    def setFood(self,food='omelet'):
        self.food = food
    # Setter for the drink
    def setDrink(self,drink='coffee'):
        self.drink = drink
    # Setter for the name
    def setName(self,name=''):
        self.name = name

class Breakfast(Meal):
    '''
    holds the food and drink for breakfast.
    '''
    def __init__(self):
        Meal.__init__(self,'omelet','coffee')
        self.setName('breakfast')

class Lunch(Meal):
    '''
    holds the food ank drink for lunch.
    '''
    def __init__(self):
        '''
        Initialize the food and drink for lunch
        '''
        Meal.__init__(self,'sandwich','gin and tonic')
        self.setName('lunch')

    #重写setFood方法
    def setFood(self,food='sandwich'):
        if food !='sandwich' and food != 'omelet':
            raise AngryChefException
        Meal.setFood(self,food)

class Dinner(Meal):
    def __init__(self):
        '''
        Initialize with steak and merlot.
        '''
        Meal.__init__(self,'steak','merlot')
        self.setName('dinner')

    def printIt(self,prefix=''):
        '''
        Print even more nicely.
        :param prefix:
        :return:
        '''
        print(prefix,'A gourmet',self.name,'with',self.food,'and',self.drink)

def test():
    '''Test function.'''
    print('Module meal test.')
    #Generic no arguments.

    print('Testing Meal class.')
    m = Meal()
    m.printIt('\t')
    m = Meal('green eggs and ham','tea')
    m.printIt('\t')

    #Test breakfast
    print('Testing Breakfast class.')
    b = Breakfast()
    b.printIt('\t')

    b.setName('breaking of the fast')
    b.printIt('\t')

    #Test dinner
    print('Testing Dinner class')
    d = Dinner()
    d.printIt('\t')

    #Test lunch
    print('Testing Lunch class')
    l = Lunch()
    l.printIt('\t')
    print('Calling lunch.setFood().')
    try:
        l.setFood('hotdog')
    except AngryChefException:
        print('\t'),'The chef is angry.Pick an omelet'
#Run test if this module is run as a program.
if __name__ == '__main__':
    test()