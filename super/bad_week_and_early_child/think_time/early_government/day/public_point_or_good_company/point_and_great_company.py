
#! /usr/bin/env python

def woman(str_arg):
    small_place(str_arg)
    print('long_part')

def small_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('number')
