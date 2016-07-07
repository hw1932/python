def do_plus(a,b):
    if type(a)==type(b)==type(1):
        print('the two arguments are int')
        return a+b

    elif type(a)==type(b)==type('1'):
        print('the two arguments are str')
        return a+b
    else:
        raise TypeError('No such arguments type:"%s",%s' %(a,b))
 #       return 'raise TypeError, please check out'
print(do_plus('abc',1))