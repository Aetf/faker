
#! /usr/bin/env python

def see_case(str_arg):
    try_place(str_arg)
    print('do_place')

def try_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_case('group')
