#coding=utf-8
import pickle as p

def load_packle(n=1,sex='boy'):
    #'n代表第几段对话，代表要女孩还是男孩的话'
    file_path = sex+'_'+str(n)+'.pickle'
    f = open(file_path,'rb')
    boy1 = p.load(f)
    print(sex+'_'+str(n),boy1)

if __name__ == '__main__':
    #load_packle(3,'girl')
    load_packle(3)