#coding=utf-8
import easygui as g
import sys

msg = 'this is the msg'
title = 'this is the title'
image = '1.gif'
file = 'E:\\PyCharm4.5_workspace\\excerse\\05\\1.javac'
dire = 'E:\\PyCharm4.5_workspace\\excerse\\05'
enter = '请在此处输入您希望的内容'
choices2 = ['是','否']
choices3 = ['b1','b2','b3']
choices4 = ['b1','b2','b3','b4']
choices5 = ['b1','b2','b3','b4','b5']
choices6 = ['b1','b2','b3','b4','b5','b6']
choices9 = ['b1','b2','b3','b4','b5','b6','b7','b8','b9']
#file_types从下面的例子可以得到，字符串二级字符串列表的最后一个是对前面多个类型的总描述
#可以有多个二级字符串列表
#'al_file'这个描述没有成功，因为他是一级列表，认为是一个匹配类型，和'*.html'等价
#openfilebox()方法第一个参数file中是'1,javac'类型，
# 后面的file_types可以不再定义，在选择框中会出现*.javac选项
file_types = ['*.html', '*.css', '*.txt', ['*.jpg','*.gif','Picture'],
              ['*.py','*.pyc','Python files'], 'al_file']

def p(c):
    '''
    打印c的值和类型
    :param c:
    :return:
    '''
    print(type(c))
    print(c)
    return

def boolboex():
    c = g.boolbox(msg,title,choices2,image)
    p(c)

def buttonbox():
    c = g.buttonbox(msg,title,choices6,image)
    p(c)

def ynbox():
    c = g.ynbox(msg,title,choices2,image)
    p(c)

def choicebox():
    c = g.choicebox(choices=choices6)
    p(c)

def codebox():
    c = g.codebox(msg,title,'123\n456\t789')
    p(c)

def diropenbox():
    c = g.diropenbox(msg,title,dire)
    p(c)

def enterbox():#strip用法
    c = g.enterbox(msg,title,enter,image=image)
    p(c)

def exceptionbox():
    try:
        int('abc')
    except:
        c = g.exceptionbox()
    p(c)

def fileopenbox():
   c = g.fileopenbox(default=file,filetypes=file_types)
   p(c)

def filesavebox():
    c = g.filesavebox(default=file,filetypes=file_types)
    p(c)

def indexbox():
    c = g.indexbox(choices=choices5,image=image)
    p(c)

def integerbox():
    c = g.integerbox(lowerbound=1,upperbound=100,image=image)
    p(c)

def msgbox():
    c = g.msgbox(msg,title,ok_button='你敢点？',image=image)
    p(c)

def multchoicebox():
    c = g.multchoicebox(choices=choices9)
    p(c)

def multenterbox():
    c = g.multenterbox(fields=choices5,values=choices4)
    p(c)

def multpasswordbox():
    c = g.multpasswordbox(fields=choices5,values=choices4)
    p(c)

def passwordbox():
    c = g.passwordbox(default='default',image=image)
    p(c)

def read_or_create_settings():
    c = g.read_or_create_settings('c:/a.log')
    p(c)

class Egstore(g.EgStore):
    def __init__(self,filename):
        self.filename = filename

def set(filename):
    seting = Egstore(filename)
    seting.userId = file
    seting.server = dire
    seting.store()
    print(seting.userId,seting.server,seting.last_time_stored,seting.filename)

if __name__ == '__main__':
    #boolboex()
    #buttonbox()
    #ynbox()
    #choicebox()
    #codebox()
    #diropenbox()
    #enterbox()
    #exceptionbox()
    #multenterbox()
    #fileopenbox()
    #filesavebox()
    #indexbox()
    #integerbox()
    #msgbox()
    #multchoicebox()
    #multpasswordbox()
    #passwordbox()
    #read_or_create_settings()
    set(file)
