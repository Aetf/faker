
#! /usr/bin/env python

def say_great_time(str_arg):
    first_point(str_arg)
    print('different_point')

def first_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_great_time('have_problem')
