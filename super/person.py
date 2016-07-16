
#! /usr/bin/env python

def long_thing(str_arg):
    person(str_arg)
    print('same_day')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_thing('great_life')
