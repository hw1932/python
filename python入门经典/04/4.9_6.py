#coding=utf-8

fridge={'apple':"red",'checken':"new",'milk':"white"}
b=1
try:
    if fridge['meat']=='red':
        print('meat is red')
except (TypeError,KeyError) as error:
    print ('the %s is not in fridge.keys'%error)
else:
    print('meat  in fridge.keys()')


def b():
    '''
    这是文档说明字符串
    '''
    i = b+1
    print (i)
    return b+1
print ('%s'%b.__doc__)
print(b())