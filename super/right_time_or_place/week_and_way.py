
#! /usr/bin/env python

def see_long_thing(str_arg):
    fact(str_arg)
    print('early_fact')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_long_thing('number')
