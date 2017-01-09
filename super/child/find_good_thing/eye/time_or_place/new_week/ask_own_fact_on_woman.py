
#! /usr/bin/env python

def hand(str_arg):
    call_small_work(str_arg)
    print('way')

def call_small_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('small_problem')
