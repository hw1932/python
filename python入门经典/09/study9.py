import sys,os,string

a = [1,2,3,4,5,6,7,8]
print([x for x in a if x%2==0])

print(range(1,11,2),'\n',range(1,11,2)[0],*range(1,10))

d = {'1':1,'2':2,'c':3,'d':4}#key不可以是数字
print('the number is %(1)d,%(2)d,%(c)d,%(d)d'%d)

person = {'a':1,'b':2,'c':3,'d':4}#key不可以是数字
person['e'] = 5
person['f'] = 6
t = string.Template('$a=1,$b=2,$e=5,$f=6')
print (t.substitute(person))

def comm():#调用系统命令行终端
    if sys.platform == 'win32':
        print('running on a windows platform!')
        command = 'cmd.exe'
    if sys.platform == 'linux2':
        print('running Linux')
        command = 'uname -a'
    os.system(command)

def process_my():
    pid = os.fork()
    print('second test')
    if  pi == 0:
        print('this is the child')
        print('I`m going to  exec another program now')
        os.execl('c:/bin')


