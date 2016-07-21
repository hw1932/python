#coding:utf-8
f = open('record.txt')
#用列表存储所需的内容
boy = []
girl = []
#计数器，计算第几段对话
count = 1

for each_line in f:
    if each_line[:6] != '======':
        #这里进行字符串分割操作
        (role,line_spoken) = each_line.split('：')
        if role == '小甲鱼':
            boy.append(line_spoken)
        elif role == '小客服':
            girl.append(line_spoken)
    else:#each_line[:6]=='===='成立时，下面开始执行保存
    #生成指定的文件名
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'
    #打开文件
        boy_file = open(file_name_boy,'w')
        girl_file = open(file_name_girl,'w')
    #writelines方法用于序列化的写操作
        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
    #初始化
        boy = []
        girl = []
        count +=1

f.close()