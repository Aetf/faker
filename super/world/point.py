
#! /usr/bin/env python

def able_thing(str_arg):
    bad_group(str_arg)
    print('next_number_and_group')

def bad_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    able_thing('thing')
