
#! /usr/bin/env python

def call_early_problem(str_arg):
    fact(str_arg)
    print('bad_man')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_early_problem('able_world')
