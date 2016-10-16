
#! /usr/bin/env python

def company_and_great_place(str_arg):
    long_way(str_arg)
    print('child')

def long_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company_and_great_place('public_work')
