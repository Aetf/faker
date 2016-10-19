
#! /usr/bin/env python

def child(str_arg):
    group_or_time(str_arg)
    print('point')

def group_or_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('group')
