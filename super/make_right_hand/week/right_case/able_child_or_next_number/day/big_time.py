
#! /usr/bin/env python

def leave_problem_from_new_group(str_arg):
    fact_or_case(str_arg)
    print('child')

def fact_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_problem_from_new_group('old_case')
