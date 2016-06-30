
#! /usr/bin/env python

def child_and_thing(str_arg):
    part(str_arg)
    print('child_and_case')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_thing('thing_and_bad_fact')
