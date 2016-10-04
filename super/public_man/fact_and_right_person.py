
#! /usr/bin/env python

def thing(str_arg):
    old_thing(str_arg)
    print('government')

def old_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('number')
