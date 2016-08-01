
#! /usr/bin/env python

def last_thing(str_arg):
    man(str_arg)
    print('public_way')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_thing('do_fact')
