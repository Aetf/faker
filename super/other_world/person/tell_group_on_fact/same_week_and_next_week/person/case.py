
#! /usr/bin/env python

def big_problem_and_large_case(str_arg):
    first_problem(str_arg)
    print('do_next_thing')

def first_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_problem_and_large_case('other_world')
