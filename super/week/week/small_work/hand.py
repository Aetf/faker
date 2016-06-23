
#! /usr/bin/env python

def work_child(str_arg):
    get_great_world(str_arg)
    print('life')

def get_great_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('company')
