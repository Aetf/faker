
#! /usr/bin/env python

def thing(str_arg):
    big_child(str_arg)
    print('number')

def big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('right_place')
