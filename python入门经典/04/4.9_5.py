#coding=utf-8
fridge={'apple':"red",'checken':"new",'milk':"white"}
fridge_list = list(fridge.keys())
while len(fridge_list)>0:
    current_key = fridge_list.pop()
else:
    print('%s is in fridge_list'%current_key)