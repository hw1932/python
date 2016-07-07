#coding=utf-8
import csv,os

read():
    file_path = 'address_book.csv'
    if os.path.exists(file_path) is True:
        csv_file = open(file_path,'rb')
        read = csv.reader(csv_file)
        for person in read:
            print person
    else:
        print('文件不存在或路径错误')
read()