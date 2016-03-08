
#! /usr/bin/env python

def know_own_child_from_problem(str_arg):
    problem(str_arg)
    print('own_child')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    know_own_child_from_problem('thing')
