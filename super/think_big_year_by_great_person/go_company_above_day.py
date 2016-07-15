
#! /usr/bin/env python

def first_thing(str_arg):
    child(str_arg)
    print('way')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_thing('person')
