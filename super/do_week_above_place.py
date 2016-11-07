
#! /usr/bin/env python

def come_big_place(str_arg):
    small_work(str_arg)
    print('old_man')

def small_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    come_big_place('make_case')
