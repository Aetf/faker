
#! /usr/bin/env python

def bad_thing(str_arg):
    right_person(str_arg)
    print('make_number')

def right_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_thing('great_number')
