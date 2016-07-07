#coding=utf-8
import os,os.path,re

def print_pdf(root,dirs,files):
    for file in files:
        path = os.path.join(root,file)
        path = os.path.normcase(path)
        if re.search(r'.*\.py',path):
            print(path)

def print_pdf2(arg,dir,files):
    for file in files:
        path = os.path.join(dir,file)
        path = os.path.normcase(path)
        if not re.search(r'.*\.pdf',path):continue
        if re.search(r' ',path):continue
        print(path)

def excerse1(arg,dir,files):
    for file in files:
        path = os.path.join(dir,file)
        path = os.path.normcase(path)
        if not re.search(r'.*\.pdf',path):continue
        if re.search(r' ',path):continue
        print(path)
#os.path.walk('/',excerse1,0)

def excerse2(arg,dir,files):
    for file in files:
        path = os.path.join(dir,file)
        path = os.path.normcase(path)
        #if re.search(r'.*boobah*\.pdf',path):continue
        if not re.search(r'.*\.pdf',path):continue
        if re.search(r'boobah',path):
            print(path)
#os.path.walk('.',excerse2,0)

def excerse3(arg,dir,files):
    for file in files:
        path = os.path.join(dir,file)
        path = os.path.normcase(path)
        if re.search(r'boobah',path):continue
        print(path)
#os.path.walk('.',excerse3,0)

def exp_1():
    s = ('xxx','abcxxxabc','xyx','abc','x.x','axa','axxxxa','axxya')
    a = filter((lambda s:re.match(r'xxx',s)),s)
    b = filter((lambda s:re.search(r'xxx',s)),s)
    d = filter((lambda s:re.search('\.',s)),s)
    e = filter((lambda s:re.search('x*x',s)),s)
    f = filter((lambda s:re.match(r'x.+x',s)),s)
    g = filter((lambda s:re.search(r'c',s)),s)
    h = filter((lambda s:re.search(r'[^c]*',s)),s)
    print('a:',*a)
    print('b:',*b)
    print('d:',*d)
    print('e:',*e)
    print('f:',*f)
    print('h:',*h)

def dir():
    #把本文件当前目录下的文件按空格和制表符分隔并打印出来
    f = os.popen('dir','r')
    for eachline in f.readlines():
        print(re.split('\s\s+|\t',eachline.strip()))#strip去掉换行符
    f.close()

if __name__ == '__main__':
    #exp_1()
    #os.path.walk('/',print_pdf2,0)
    dir()