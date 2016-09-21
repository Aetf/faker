
#! /usr/bin/env python

def number(str_arg):
    old_problem(str_arg)
    print('child')

def old_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number('number')
