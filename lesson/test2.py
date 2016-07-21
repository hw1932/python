#coding:utf-8
def p():
    print('我是p方法，在if后面，我是从当前文件运行的')

def q():
    print('我是q方法，在else后面，我不是从当前文件运行的')
if __name__ == '__main__':
    p()

else:
    q()
    print('__name__ ->  %s'%__name__)