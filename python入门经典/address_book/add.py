#coding=utf-8
import csv,os
add():
    '''Add a person to the list'''
    global all_person
    name = input('Enter the name:')
    for i in range(0,len(all_person))s
        if len(all_person[i][0]) == 0:
            continue
        elif all_person[i][0] == name:
            name = input('Person already exists,please try again:')
            break
    age = input('Enter the age:')
    number = input('Enter the number:')
    all_person.append([name,age,number])

    display()

