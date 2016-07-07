#coding=utf-8
fridge={'apple':"red",'checken':"new",'milk':"white"}
for i in fridge.keys():
    if i == 'food_sought':
        print(i)
        break
    else:
        print('food_sought != %s'%i)