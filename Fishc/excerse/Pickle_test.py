#coding=utf-8
import pickle as p

boy_list = []
girl_list = []
count = 1

def save_pickle():#文件分别保存操作
    global boy_list,girl_list,count
    file_name_boy = 'boy_' + str(count) + '.pickle'
    file_name_girl = 'girl_' + str(count) + '.pickle'

    f = open(file_name_boy,'wb')
    p.dump(boy_list,f)
    f.close()
    f = open(file_name_girl,'wb')
    p.dump(girl_list,f)
    f.close()
    boy_list = []
    girl_list = []
    count +=1

f = open('record.txt','r')
for each_line in f:
    if each_line[:6] != '======':
        role,spoken = each_line.split('：')
        if role == '小甲鱼':
            boy_list.append(spoken)
        elif role == '小客服':
            girl_list.append(spoken)
    else:#文件分别保存操作
        save_pickle()

f.close()
save_pickle()#第三个对话没有=====，不会触发保存操作，所以显式添加保存操作


