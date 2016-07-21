#coding:utf-8
import pickle
filepath = r'E:\PyCharm4.5_workspace\Project\Fishc\31.pickle'


def pickle_save():
    #my_list = [123,3,14,'小甲鱼',[123,'123']]
    my_list = input('请输入想要保存的内容')
    pickle_file = open(filepath,'wb')
    pickle.dump(my_list,pickle_file)
    pickle_file.close()

def pickle_load():
    pickle_file = open(filepath,'rb')
    my_list2 = pickle.load(pickle_file)
    print(my_list2)

if __name__ == '__main__':
    pickle_save()
    pickle_load()