
#! /usr/bin/env python

def person(str_arg):
    tell_fact(str_arg)
    print('right_fact')

def tell_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('little_year')
