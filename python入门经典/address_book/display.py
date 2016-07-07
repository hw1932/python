#coding=utf-8
import csv,os

def display():
    '''Display all person'''
    print('The following are all the person in your address book:')
    for person in all_person:
        print (person)
    print('')