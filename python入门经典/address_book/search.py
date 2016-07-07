#coding=utf-8
import csv,os

def search():
    #global all_person
    has_person = False
    name = input('Enter the name:')
    for person in all_person:
        if len(person) == 0:
            continue
        elif person[0] == name:
            display
            has_person = True
            break

    if not has_person:
        print('您输入的姓名在通讯录中不存在。')



search()