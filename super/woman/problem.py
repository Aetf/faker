
#! /usr/bin/env python

def do_last_time(str_arg):
    tell_last_man_by_small_time(str_arg)
    print('child')

def tell_last_man_by_small_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_last_time('first_government')
