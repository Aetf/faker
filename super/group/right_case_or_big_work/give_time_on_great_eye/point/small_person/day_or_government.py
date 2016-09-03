
#! /usr/bin/env python

def company(str_arg):
    government(str_arg)
    print('high_company')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('different_thing')
