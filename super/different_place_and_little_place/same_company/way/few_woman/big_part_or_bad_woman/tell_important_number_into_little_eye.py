
#! /usr/bin/env python

def small_time(str_arg):
    young_time(str_arg)
    print('problem')

def young_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_time('bad_child')
