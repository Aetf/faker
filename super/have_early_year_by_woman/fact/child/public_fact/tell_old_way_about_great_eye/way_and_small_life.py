
#! /usr/bin/env python

def child(str_arg):
    work_and_first_problem(str_arg)
    print('problem_or_fact')

def work_and_first_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('be_other_case')
