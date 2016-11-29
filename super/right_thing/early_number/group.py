
#! /usr/bin/env python

def other_thing(str_arg):
    thing(str_arg)
    print('able_man')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_thing('high_fact')
