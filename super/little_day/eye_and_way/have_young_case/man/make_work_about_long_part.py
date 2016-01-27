
#! /usr/bin/env python

def old_case(str_arg):
    long_case_or_thing(str_arg)
    print('bad_point')

def long_case_or_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_case('take_case_with_important_man')
