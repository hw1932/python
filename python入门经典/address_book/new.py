# codiing:utf-8
import os,csv,pickle

class Person:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def display_me(self):
        print('{name:10}{age:10}{number}'.format(
            name=self.name, age=self.age, number=self.number))

all_person = []


# The main menu of address book

def menu():
    print("Please enter the menu in front of the number.")
    print("For example,Pree '1' Add a person. ")
    print("1.Add a person.")
    print("2.Delete a person.")
    print("3.Modify a person.")
    print("4.Display all person.")
    print("5.Save the data.")
    print("6.Save and quit.")
    print("7.Search a persin.")

# load data.


def load_data():
    global all_person
    if os.path.exists('address_book.') is True:
        input_file = open('address_book.csv', 'rb')
        read = csv.reader(input_file)
        for person in read:
            all_person.append(person)
            #all_person = pickle.Unpickler(input_file).load()
        input_file.close()

# save data.


def save_data():
    output_file = open("address_book.data", 'wb')
    p = pickle.Pickler(output_file)

    print(type(all_person))
    p.dump(all_person)
    output_file.close()
    print('save sucess!')

# add person.


def add():
    '''Add a person to the list'''
    name = input('Enter the name:')
    for person in all_person:
        if person.name == name:
            name = input('Person already exists,please try again:')
            break

    age = input('Enter the age:')
    number = input('Enter the number:')
    person = Person(name, age, number)

    all_person.append(person)
    for person in all_person:
        person.display_me()

# display all person.


def display():
    '''Display all person'''
    print('The following are all the person in your address book:')
    print('{0:10}{1:10}{2:10}'.format('Name', 'Age', 'number'))
    for person in all_person:
        person.display_me()
    print('')


def delete():
    name = input('Enter the name of the person that you want to delete:')
    global all_person
    has_person = False
    for i in range(0, len(all_person)):
        if all_person[i].name == name:
            del all_person[i]
            has_person = True
            break
    if not has_person:
        print("您输入的姓名在通讯录中不存在。")

"""

更新person。
"""


def update(person, name):
    person.name = name
    person.age = input('Enter the age:')
    person.number = input('Enter the number:')


def search():
    name = input('Enter the name you want to search:')
    global all_person
    has_person = False
    for i in range(0, len(all_person)):
        if all_person[i].name == name:
            print("查询结果如下：")
            all_person[i].display_me()
            has_person = True
            break
    if not has_person:
        print("找不到姓名为%s的人" % all_person[i].name)


def modify():
    '''modify the person by person name'''
    name = input('Enter the name you want to modify:')
    global all_person
    for i in range(0, len(all_person)):
        if all_person[i].name == name:
            update(all_person[i], name)
            print('Done!')


load_data()
menu()
while True:
    oper = input()

    if oper == '1':
        add()
        print("输入'm'返回主菜单")
    elif oper == '2':
        delete()
        print("输入'm'返回主菜单")
    elif oper == '3':
        modify()
        print("输入'm'返回主菜单")
    elif oper == '4':
        display()
        print("输入'm'返回主菜单")
    elif oper == '5':
        save_data()
        print("输入'm'返回主菜单")
    elif oper == '6':
        save_data()
        print("输入'm'返回主菜单")
        break
    elif oper == '7':
        search()
        print("输入'm'返回主菜单")
    elif oper == 'm':
        menu()
    else:
        print("您的输入有误。")
