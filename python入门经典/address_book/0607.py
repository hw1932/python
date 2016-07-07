#coding=utf-8
import csv,os

class Person:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def display_me(self):
        print('{name:10}{age:10}{number}'.format(
            name=self.name, age=self.age, number=self.number))

all_person = []
'''
read():
    file_path = 'address_book.csv'
    if os.path.exists(file_path) is True:
        csv_file = open(file_path,'rb')
        read = csv.reader(csv_file)
        for person in read:
            print person
    else:
        print('文件不存在或路径错误')
'''


def add():
    #Add a person to the list
    global all_person
    file_path = 'address_book.csv'
    csv_file = open(file_path, 'rb+')
    reader = csv.reader(csv_file)
    writer = csv.writer(csv_file)

    #writer.writerow(['姓名','年龄','电话'])

    name = input('Enter the name:')
    for person in reader:
        if len(person) == 0:
            continue
        elif person[0] == name:
            name = input('Person already exists,please try again:')
            break

    age = input('Enter the age:')
    number = input('Enter the number:')
    data = [name,age,number]
    writer.writerow(data)


    csv_file.seek(0)
    for person in reader:
        print (person)
    csv_file.close()
add()