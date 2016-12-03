
#! /usr/bin/env python

def life(str_arg):
    hand(str_arg)
    print('own_thing')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('fact_or_problem')
