
#! /usr/bin/env python

def long_child(str_arg):
    different_problem(str_arg)
    print('call_day')

def different_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_child('other_life')
