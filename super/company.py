
#! /usr/bin/env python

def public_fact(str_arg):
    tell_fact(str_arg)
    print('small_company')

def tell_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_fact('fact')
