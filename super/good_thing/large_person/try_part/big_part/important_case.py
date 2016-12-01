
#! /usr/bin/env python

def group(str_arg):
    first_problem(str_arg)
    print('other_group')

def first_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('person')
