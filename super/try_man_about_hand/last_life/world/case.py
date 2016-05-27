
#! /usr/bin/env python

def old_thing(str_arg):
    great_part(str_arg)
    print('get_case')

def great_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_thing('new_world')
