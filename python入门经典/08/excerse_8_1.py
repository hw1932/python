#coding=utf-8
import os,glob

#glob方法，只输出目录和文件名，不包含路径
def print_dir_only_name():
    path = 'E:\\PyCharm4.5_workspace\\excerse\\'
    list = sorted(glob.glob(path+'[!.]'))
    list_dir = []
    list_file = []

    for p in list:
        if os.path.isdir(p):
            list_dir.append(p)
        elif os.path.isfile(p):
            list_file.append(p)

    for i in range(0,len(list_dir)):
        list_dir[i] = os.path.split(list_dir[i])[1]

    list_file = sorted(glob.glob(path+'*.*'))
    for i in range(0,len(list_file)):
        list_file[i] = os.path.split(list_file[i])[1]

    print('------------')
    print('目录：',list_dir)
    print('文件：',list_file)

#glob，返回名称，含路径
def print_dir_by_glob():
    path = 'E:\\PyCharm4.5_workspace\\excerse\\'
    list = sorted(glob.glob(path+'*'))
    list_directory = []
    list_file = []

    for i in range(0,len(list)):
        if os.path.isdir(list[i]):
            list_directory.append(list[i])
        elif os.path.isfile(list[i]):
            list_file.append(list[i])

    print('------------')
    print('目录：',list_directory)
    print('文件：',list_file)
    return

if __name__ == '__main__':
    print_dir_only_name()
    print_dir_by_glob()
