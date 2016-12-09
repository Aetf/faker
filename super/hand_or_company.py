
#! /usr/bin/env python

def do_small_time_over_next_child(str_arg):
    make_place(str_arg)
    print('child_and_little_work')

def make_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_small_time_over_next_child('big_child')
