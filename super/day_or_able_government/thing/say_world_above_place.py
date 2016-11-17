
#! /usr/bin/env python

def long_man(str_arg):
    young_man(str_arg)
    print('problem')

def young_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_man('great_child')
