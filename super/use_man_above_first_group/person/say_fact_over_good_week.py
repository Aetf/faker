
#! /usr/bin/env python

def small_thing(str_arg):
    way(str_arg)
    print('person')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_thing('different_way')
