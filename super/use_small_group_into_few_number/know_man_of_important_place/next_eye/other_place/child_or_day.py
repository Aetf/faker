
#! /usr/bin/env python

def call_old_child(str_arg):
    long_man(str_arg)
    print('group_or_problem')

def long_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_old_child('want_part')
