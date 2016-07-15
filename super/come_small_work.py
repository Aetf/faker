
#! /usr/bin/env python

def hand_or_thing(str_arg):
    feel_thing_at_case(str_arg)
    print('new_case')

def feel_thing_at_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand_or_thing('person')
