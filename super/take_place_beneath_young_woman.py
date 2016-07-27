
#! /usr/bin/env python

def big_thing(str_arg):
    public_case(str_arg)
    print('government')

def public_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('man')
