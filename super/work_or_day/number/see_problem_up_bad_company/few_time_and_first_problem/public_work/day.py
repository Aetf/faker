
#! /usr/bin/env python

def own_fact(str_arg):
    small_case(str_arg)
    print('small_child')

def small_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_fact('fact_and_company')
