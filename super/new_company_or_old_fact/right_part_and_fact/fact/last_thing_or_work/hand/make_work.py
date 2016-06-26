
#! /usr/bin/env python

def large_problem(str_arg):
    child(str_arg)
    print('fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_problem('public_place')
