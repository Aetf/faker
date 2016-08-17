
#! /usr/bin/env python

def fact(str_arg):
    point_or_problem(str_arg)
    print('early_fact')

def point_or_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('long_group')
