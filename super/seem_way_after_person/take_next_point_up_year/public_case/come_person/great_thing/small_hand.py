
#! /usr/bin/env python

def have_problem(str_arg):
    work_group(str_arg)
    print('early_world')

def work_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_problem('own_case')
