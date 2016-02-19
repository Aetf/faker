
#! /usr/bin/env python

def company(str_arg):
    government(str_arg)
    print('number_or_small_company')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('child')
