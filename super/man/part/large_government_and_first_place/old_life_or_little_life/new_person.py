
#! /usr/bin/env python

def big_part(str_arg):
    fact_or_person(str_arg)
    print('child')

def fact_or_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_part('public_life')
