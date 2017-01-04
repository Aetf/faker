
#! /usr/bin/env python

def small_company(str_arg):
    long_way(str_arg)
    print('be_new_way')

def long_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_company('want_different_company')
