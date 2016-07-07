# coding=utf-8
import os,csv

all_person = []
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
#load()
def load_data():
    global all_person
    if os.path.exists('address_book.csv') is True:
        input_file = open('address_book.csv', 'r+')
        read = csv.reader(input_file)
        for person in read:
            if len(person) > 0:
                all_person.append(list(person))
        input_file.close()
        print ('load success')
    else:
        print ('not exist!')
    display()
#save
def save_data():
    #global all_person
    output_file = open("address_book_1.csv", 'w+')
    write = csv.writer(output_file)
    write.writerows(all_person)
    output_file.close()
    print ('save success!')

#add()
def add():
    '''Add a person to the list'''
    global all_person
    name = input('Enter the name:')
    while len(name) == 0:
        name = input('Enter the name which is not None:')
    # for i in range(0,len(all_person)):
    #     if len(all_person[i][0]) == 0:
    #         continue
    #     elif all_person[i][0] == name:
    for person in all_person:
        if  len(person) > 0:
            if person[0] == name:
                name = input('Person already exists,please try again:')
                break
    age = input('Enter the age:')
    number = input('Enter the number:')
    all_person.append([name,age,number])
    print('success add!')
    display()

def display():
    '''Display all person'''
    print('The following are all the person in your address book:')
    for person in all_person:
        print (person)
    print('')

def delete():
    global all_person
    name = input('Enter the name:')
    has_person = False

    for i in range(0, len(all_person)):
        if all_person[i][0] == name:
            del all_person[i]
            has_person = True
            print ('delete success')
            break

    if not has_person:
        print('您输入的姓名在通讯录中不存在。')
    display()

def modify():
    global all_person
    name = input('Enter the name:')
    has_person = False

    for i in range(0, len(all_person)):
        if len(all_person[i][0])==0:
            continue
        elif all_person[i][0] == name:
            all_person[i][1] = input('Enter the age:')
            all_person[i][2] = input('Enter the number:')
            has_person = True
            print ('success update')
            break

    if not has_person:
        print('您输入的姓名在通讯录中不存在。')
    display()

def search():
    #global all_person
    has_person = False
    name = input('Enter the name:')
    for person in all_person:
        if len(person) == 0:
            continue
        elif person[0] == name:
            print (person)
            has_person = True
            print ('search success')
            break

    if not has_person:
        print('您输入的姓名在通讯录中不存在。')

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