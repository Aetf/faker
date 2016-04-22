
#! /usr/bin/env python

def try_early_problem_beneath_own_group(str_arg):
    child(str_arg)
    print('other_group')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_early_problem_beneath_own_group('few_number')
