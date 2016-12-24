
#! /usr/bin/env python

def thing(str_arg):
    make_bad_day(str_arg)
    print('first_thing')

def make_bad_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('young_part')
