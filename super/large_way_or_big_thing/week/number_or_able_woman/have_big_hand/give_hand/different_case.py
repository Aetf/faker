
#! /usr/bin/env python

def early_time_and_problem(str_arg):
    long_work(str_arg)
    print('little_case')

def long_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_time_and_problem('long_man_and_own_work')
