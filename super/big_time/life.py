
#! /usr/bin/env python

def call_large_life(str_arg):
    own_life(str_arg)
    print('other_way')

def own_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_large_life('do_company_over_child')
