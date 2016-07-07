#coding=utf-8
#from easygui import easygui as g
import easygui as g
import  sys
import re

msg = '这是一个msg信息'
title = '这是title'

def easygui_excerse():
    while 1:
        g.msgbox('hi,wellcom to the first game')
        msg = 'what do you want to learn ? '
        title = 'little game'
        choices = ['love', 'program', 'ooxx', 'reading']

        choice = g.choicebox(msg,title,choices)

        #注意我们换成了字符串，以防用户取消选择，我们什么也没得到
        g.msgbox('your choice is :' + str(choice), 'result')

        msg = 'do u wish restart the game?'
        title = 'please select'

        if  g.ccbox(msg,title): #show a Continue/Cancel dialog
            pass                #user choose Continue
        else:
            sys.exit(0)         #user choose Cancel

def msgbox_2():
    g.msgbox(msg='Yes, I can', ok_button='you can~!')

def ccbox_2():
    if g.ccbox(msg='do you want continue?',title='choose',choices=('yao','buyao')):
        g.msgbox('结束了，不给玩了',ok_button='想玩就再点我')
    else:
        sys.exit(0)

def buttonbox_2():
    msg = 'which do you like?'
    title = ''
    choices = ('b1','b2','b3')
    choice = g.buttonbox(msg,title,choices)
    print(choice)

def multchoicebox():
    msg = '这是复选'
    title ='练习'
    choices = ['b1','b2','b3','b4']
    choice = g.multchoicebox(msg,title,choices)
    print(choice)

def enterbox():
    msg = 'please enter the words'
    title = 'excerse_enter'

    enter_word = g.enterbox(msg=msg,title=title,image='1.gif')
    print(enter_word)

def integerbox():
    msg = '请输入整形数'
    title = '数字'
    lowerbound = 0
    upperbound = 100
    n = g.integerbox(msg,title,lowerbound=lowerbound,upperbound=upperbound,image='1.gif')
    print(n)

def multinterbox():
    msg = ('请输入对应的数据',
          '*真实姓名',
          '手机号码',
          '邮箱')
    title = '帐号中心'
    m = g.multenterbox(msg,title,['*手机号','*姓名','*邮箱','固话','QQ'],values=['1','2','3'])
    print(m)

def multpassword():
    msg = 'My dear customer,wellcome login !'
    title = 'login'
    fields = ('*用户名','*密码','安全码')#可以有多个，只有最后一个用户输入时是****
    values = ('请在此处输出您的用户名','请在此处输入您的密码','安全码')
    m = g.multpasswordbox(msg,title,fields,values)
    print(m)

def textbox():
    m = g.textbox(msg,title,text=['2131231222\n123131  ','AAAAA1231\n32\n  ','123'],codebox=1)
    print(m)

def codebox():
    m = g.codebox(msg,title,text=['2131231222\n123131  ','AAAAA1231\n32\n  ','123'])
    print(m)

def diropenbox():
    m = g.diropenbox(msg,title,default='C:/python27')
    print(m)

def fileopenbox():
    #m = g.fileopenbox(msg,title,default=r'E:\PyCharm4.5_workspace\excerse\05\*.py')
    m = g.fileopenbox(msg,title,default='E:\\PyCharm4.5_workspace\\excerse\\05\\test*.py')
    print(m)

# class Set(g.EgStore):
#     def __init__(self,filename='c:/*.*'):
#         self.filename = filename
#
# def EgStore():
#     settingfilename = 'E:\\PyCharm4.5_workspace\\excerse\\05\\test111.py'
#     settings = Set(settingfilename)
#     user = '奥巴马'
#     server = '白宫'
#     settings.userId = user
#     settings.targetServer = server
#     settings.store()
#
#     print(settings.filename,settings.userId,settings.targetServer,settings.last_time_stored)
#
#     user = '鲁大师'
#     settings.userId = user
#     settings.store()
#     print(settings.userId,settings.last_time_stored)

class Set(g.EgStore):
    def __init__(self,filename):
        self.filename = filename

def eg_store():
    settings = Set('d:/demo.py')
    settings.userId = 123
    settings.server = 456
    settings.store()
    print(settings.userId,settings.server,settings.filename,settings.last_time_stored)
def exceptionbox():
    try:
        int('aac')
    except:
        g.exceptionbox()


if __name__ == '__main__':
    #easygui_excerse()
    #g.egdemo()
    #msgbox_2()
    #ccbox_2()
    #buttonbox_2()
    #print(g.indexbox('选一个想吃的','这是主题',('草莓','西瓜','苹果')))
    #print(g.boolbox(msg='约？',title='抉择吧',choices=('约','不约')))
    # print(g.buttonbox(msg='join?',
    #                   title='choose',
    #                   choices=('okay','No!','let me think'),
    #                   image=r'E:\PyCharm4.5_workspace\excerse\GUI\1.gif'))
    #print(g.choicebox(msg='去哪吃',title='选择吃饭地点',choices=('b1','b2','b3','b4','b5','b6','b7')))
    #print(g.choicebox(msg='去哪吃',title='选择吃饭地点',choices=['b1','b2','b3','b4','b5','b6','b7']))
    #multchoicebox()
    #enterbox()
    #integerbox()
    #multinterbox()
    #print(g.passwordbox(msg='enter your password',title='login',image='1,gif'))
    #multpassword()
    #textbox()
    #codebox()
    #diropenbox()
    #fileopenbox()
    #g.fileopenbox(msg,title,filetypes=['*.css','*.javac',['*.java','*.html','*.py']])
    #g.filesavebox(default='E:/test*.py',filetypes=['*.css','*.html',['*.py','python files']])
    #exceptionbox()
    eg_store()



