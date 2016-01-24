
#! /usr/bin/env python

def small_problem(str_arg):
    new_time(str_arg)
    print('child')

def new_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_problem('use_time')
