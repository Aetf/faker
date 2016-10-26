
#! /usr/bin/env python

def person_or_long_thing(str_arg):
    other_part(str_arg)
    print('part')

def other_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person_or_long_thing('person')
