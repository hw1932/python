#coding=utf-8
import pickle as p

def pickle_save():
    my_list = [[[123],123,'abc'],123,'abc']
    f = open('test714.pickle','wb')
    p.dump(my_list,f)
    f.close()


def pickle_load():
    with open('test714.pickle','rb') as f:
        content = p.load(f)
    print(content)

if __name__ == '__main__':
    pickle_save()
    pickle_load()