
#! /usr/bin/env python

def large_thing(str_arg):
    own_case(str_arg)
    print('little_hand')

def own_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_thing('eye')
