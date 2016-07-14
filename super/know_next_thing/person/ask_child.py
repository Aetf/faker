
#! /usr/bin/env python

def able_man(str_arg):
    bad_way(str_arg)
    print('group')

def bad_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    able_man('time')
