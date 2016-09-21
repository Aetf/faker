
#! /usr/bin/env python

def life(str_arg):
    find_number(str_arg)
    print('long_child')

def find_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('other_fact')
