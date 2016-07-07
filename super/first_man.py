
#! /usr/bin/env python

def first_child(str_arg):
    great_problem(str_arg)
    print('own_problem')

def great_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_child('long_case')
