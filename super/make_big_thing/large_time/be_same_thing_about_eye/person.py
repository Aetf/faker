
#! /usr/bin/env python

def different_place(str_arg):
    thing(str_arg)
    print('group')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_place('world')
