
#! /usr/bin/env python

def first_time(str_arg):
    great_case(str_arg)
    print('see_next_person')

def great_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_time('long_thing')
