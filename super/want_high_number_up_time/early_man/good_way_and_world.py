
#! /usr/bin/env python

def small_company(str_arg):
    large_place(str_arg)
    print('big_part')

def large_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_company('week_or_next_part')
