
#! /usr/bin/env python

def other_number(str_arg):
    place(str_arg)
    print('own_part')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_number('different_thing')
