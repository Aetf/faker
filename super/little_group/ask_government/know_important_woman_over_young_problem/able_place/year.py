
#! /usr/bin/env python

def small_time(str_arg):
    child(str_arg)
    print('big_child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_time('little_man')
