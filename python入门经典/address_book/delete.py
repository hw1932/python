#coding=utf-8
import csv,os
def delete():
    name = input('Enter the name:')
    has_person = False

    for i in range(0, len(all_person)):
        if all_person[i][0] == name:
            del all_person[i]
            has_person = True
            break

    if not has_person:
        print('您输入的姓名在通讯录中不存在。')
    display()