
#! /usr/bin/env python

def government(str_arg):
    do_time(str_arg)
    print('child')

def do_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    government('long_problem_or_life')
