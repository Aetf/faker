
#! /usr/bin/env python

def bad_work(str_arg):
    problem(str_arg)
    print('public_case')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_work('government_or_number')
