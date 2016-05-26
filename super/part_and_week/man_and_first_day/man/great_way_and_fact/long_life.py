
#! /usr/bin/env python

def bad_thing(str_arg):
    great_thing_and_part(str_arg)
    print('fact')

def great_thing_and_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_thing('year')
