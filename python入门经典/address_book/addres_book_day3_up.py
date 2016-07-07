#coding=utf-8

class Person():
    def person(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_me(self):

globle all_person
all_person = []

def menu():
    print('1.Add')
    print('2.Delete')
    print('3.Modify')
    print('4.Display')

def add():
    global all_person
    name = input('Enter the name:')
    for person in all_person:
        if person.name == name:
            name = input('try again,the name exist!')
            break

    age = input('Enter the age:')
    gender = input('Enter the gender:')
    person = Person(name,age,gender)

    all_person.append(person)
    for person in all_person:
        person.display_me()

def display():
    print('all person as follows:')
    for person in all_person:
        person.display_me()
    print('')

