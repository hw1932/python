def make_omelet(omelet_type):
    '''
    做一个煎蛋
    '''
    if type(omelet_type) == type({}):
        print('omelet_type is a dic with ingredients')
        return make_food(omelet_type,'omelet')
    elif type(omelet_type) == type(''):
        omelet_ingredients = get_omelet_ingreedients(omelet_type)
        return make_food(omelet_ingredients,omelet_type)
    else:
        print('I don`t think i can make this kind of omelet:%s' %omelet_type)

def make_omelet_q3(fridge,omelet_type):
    '''
    做一个煎蛋
    '''
    if type(fridge) == type({}):
        print('fridge is a dic')
        #return make_food(omelet_type,'omelet')
   # elif type(omelet_type) == type(''):
        #97
        omelet_ingredients = get_omelet_ingreedients(omelet_type)
        #98
        return make_food(omelet_ingredients,omelet_type)
    else:
        print('I don`t think i can make this kind of omelet:%s' %omelet_type)

def remove_from_fridge(fridge,omelet_ingredients):

    for ingredients in omelet_ingredients.keys():
        if fridge[ingredients] >= omelet_ingredients[ingredients]:
            print('fridge[%s]>omelet_ingredients[%s]' %ingredients)
            fridge[ingredients]=fridge[ingredients] - omelet_ingredients[ingredients]
            print('已从冰箱中减去了%' %ingredients)
        else:
            print('firdge don`t hava enough %s'%ingredients)
            break