
#! /usr/bin/env python

def find_small_man(str_arg):
    work(str_arg)
    print('new_child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    find_small_man('do_work')
