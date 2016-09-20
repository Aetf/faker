
#! /usr/bin/env python

def bad_man(str_arg):
    time(str_arg)
    print('bad_group')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_man('world')
