
#! /usr/bin/env python

def problem(str_arg):
    tell_early_problem(str_arg)
    print('large_problem')

def tell_early_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('early_person')
