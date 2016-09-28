
#! /usr/bin/env python

def fact_or_own_life(str_arg):
    little_man(str_arg)
    print('big_time')

def little_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact_or_own_life('number')
