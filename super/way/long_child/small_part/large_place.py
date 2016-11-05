
#! /usr/bin/env python

def other_problem(str_arg):
    case(str_arg)
    print('get_long_case')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_problem('year')
