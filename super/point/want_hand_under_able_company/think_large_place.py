
#! /usr/bin/env python

def child(str_arg):
    fact_and_early_life(str_arg)
    print('same_year')

def fact_and_early_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('year')
