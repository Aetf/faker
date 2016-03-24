
#! /usr/bin/env python

def important_fact(str_arg):
    small_fact(str_arg)
    print('right_hand')

def small_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_fact('company')
