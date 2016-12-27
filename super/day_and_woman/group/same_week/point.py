
#! /usr/bin/env python

def own_thing(str_arg):
    child(str_arg)
    print('different_part')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_thing('different_fact')
