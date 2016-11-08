
#! /usr/bin/env python

def same_thing(str_arg):
    group(str_arg)
    print('same_child')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_thing('week')
