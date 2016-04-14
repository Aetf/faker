
#! /usr/bin/env python

def call_problem(str_arg):
    first_problem(str_arg)
    print('public_child_or_long_time')

def first_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_problem('child')
