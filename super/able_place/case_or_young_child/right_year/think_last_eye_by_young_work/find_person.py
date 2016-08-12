
#! /usr/bin/env python

def public_thing(str_arg):
    problem(str_arg)
    print('place')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('long_case')
