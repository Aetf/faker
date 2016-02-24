
#! /usr/bin/env python

def thing(str_arg):
    own_man(str_arg)
    print('right_child')

def own_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('government_or_important_child')
