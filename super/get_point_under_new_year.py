
#! /usr/bin/env python

def person(str_arg):
    own_case(str_arg)
    print('public_part')

def own_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('time_and_old_case')
