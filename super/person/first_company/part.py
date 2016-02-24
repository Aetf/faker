
#! /usr/bin/env python

def child(str_arg):
    group_and_man(str_arg)
    print('own_work')

def group_and_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('government')
