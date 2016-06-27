
#! /usr/bin/env python

def long_world(str_arg):
    point_or_company(str_arg)
    print('public_fact')

def point_or_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_world('other_life_and_number')
