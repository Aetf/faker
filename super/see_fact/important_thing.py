
#! /usr/bin/env python

def call_good_government(str_arg):
    small_part(str_arg)
    print('government')

def small_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_good_government('life_or_company')
