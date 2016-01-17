
#! /usr/bin/env python

def bad_problem(str_arg):
    work(str_arg)
    print('new_problem')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_problem('large_person')
