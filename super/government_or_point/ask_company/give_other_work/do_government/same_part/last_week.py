
#! /usr/bin/env python

def thing(str_arg):
    long_thing(str_arg)
    print('give_point')

def long_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('work')
