# coding:utf-8

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_me(self):
        print('{name:10}{age:10}{gender}'.format(
            name=self.name, age=self.age, gender=self.gender))

global all_person
all_person = []


# The main menu of address book

def menu():
    print('1.Add a person')
    print('2.Delet a person')
    print('3.Modify a person')
    print('4.Display all person')
    print('5.Exit')


def add():
    '''Add a person to the list'''
    name = input('Enter the name:')
    for person in all_person:
        if person.name == name:
            name = input('Person already exists,please try again:')
            break

    age = input('Enter the age:')
    gender = input('Enter the gender:')
    person = Person(name, age, gender)

    all_person.append(person)
    for person in all_person:
        person.display_me()


def display():
    '''Display all person'''
    print('The following are all the person in your address book:')
    print('{0:10}{1:10}{2:10}'.format('name', 'age', 'gender'))
    for person in all_person:
        person.display_me()
    print('')


def delete():
    '''Delete a person from the list'''
    name = input('Enter the name:')
    global all_person
    for i in range(0,len(all_person)):
        if all_person[i].name == name:
            all_person.pop(i)
    '''
        elif person.name != name:
            name = input('Person dosen`t exists,please try again:')
        else:
            print('Wrong input,back to menu!')
            break
    '''
    for person in all_person:
        person.display_me()


def update(person, name):
    #person.name = name
    person.age = input('Enter the age:')
    person.gender = input('Enter the gender')


def modify():
    '''modify the person by person name'''
    name = input('Enter the name you want to modify:')
    global all_person
    for i in range(0, len(all_person)):
        if all_person[i].name == name:
            update(all_person[i], name)
            print('Done!')



while True:
    menu()
    oper_numer = int(input())

    if oper_numer == 1:
        add()
    elif oper_numer == 2:
        delete()
    elif oper_numer == 3:
        modify()
    elif oper_numer == 4:
        display()
    elif oper_numer == 5:
	    break
    else:
        print('Wrong input,please try again')

