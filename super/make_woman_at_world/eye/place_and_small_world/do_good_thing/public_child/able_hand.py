
#! /usr/bin/env python

def old_man(str_arg):
    see_large_problem(str_arg)
    print('child')

def see_large_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_man('woman_or_year')
