
#! /usr/bin/env python

def leave_thing(str_arg):
    thing_or_great_fact(str_arg)
    print('eye')

def thing_or_great_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_thing('different_point')
