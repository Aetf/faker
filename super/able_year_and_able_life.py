
#! /usr/bin/env python

def government_or_case(str_arg):
    bad_problem(str_arg)
    print('good_place')

def bad_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    government_or_case('own_hand')
