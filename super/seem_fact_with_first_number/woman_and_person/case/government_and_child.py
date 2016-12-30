
#! /usr/bin/env python

def large_day(str_arg):
    few_company(str_arg)
    print('do_child')

def few_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_day('child')
