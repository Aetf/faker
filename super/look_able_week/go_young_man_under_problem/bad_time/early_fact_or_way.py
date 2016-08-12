
#! /usr/bin/env python

def case(str_arg):
    small_child(str_arg)
    print('big_time')

def small_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('public_man')
