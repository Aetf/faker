
#! /usr/bin/env python

def bad_life(str_arg):
    long_hand(str_arg)
    print('bad_problem')

def long_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_life('own_work')
