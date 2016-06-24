
#! /usr/bin/env python

def last_case_and_thing(str_arg):
    next_case(str_arg)
    print('bad_thing')

def next_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_case_and_thing('different_man')
