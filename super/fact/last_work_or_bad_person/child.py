
#! /usr/bin/env python

def call_world(str_arg):
    high_way(str_arg)
    print('do_child')

def high_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_world('bad_problem')
