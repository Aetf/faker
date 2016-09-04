
#! /usr/bin/env python

def child(str_arg):
    try_man_under_point(str_arg)
    print('next_number_or_next_child')

def try_man_under_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('large_thing_and_little_life')
