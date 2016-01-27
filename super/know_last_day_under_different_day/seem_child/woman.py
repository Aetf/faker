
#! /usr/bin/env python

def big_thing(str_arg):
    eye(str_arg)
    print('same_group')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('child')
