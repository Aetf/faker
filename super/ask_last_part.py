
#! /usr/bin/env python

def child(str_arg):
    group_and_eye(str_arg)
    print('say_great_number_in_large_group')

def group_and_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('early_person')
