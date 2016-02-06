
#! /usr/bin/env python

def case_or_next_problem(str_arg):
    tell_different_problem_under_large_number(str_arg)
    print('right_case')

def tell_different_problem_under_large_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case_or_next_problem('company')
