
#! /usr/bin/env python

def place(str_arg):
    high_part(str_arg)
    print('big_part')

def high_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('person')
